
pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    environment {
        PIPENV_VENV_IN_PROJECT = '1'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Comprobando codigo Python'
                sh 'python3 -m compileall -q app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Instalando dependencias y ejecutando pruebas'
                sh 'pipenv verify'
                sh 'pipenv sync --dev'
                sh 'pipenv run python -m pytest -q'
            }
        }

        stage('Generate Documentation') {
            steps {
                echo 'Generando documentacion con Doxygen'
                sh 'doxygen Doxyfile'
                sh 'test -f docs/html/index.html'
                echo 'Documentacion HTML generada correctamente'
            }
        }

        stage('Version Control') {
            steps {
                echo 'Actualizando documentacion en GitHub'

                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'github-docs-write',
                        keyFileVariable: 'DOCS_SSH_KEY'
                    )
                ]) {
                    sh '''
                        set -eu

                        git config user.name "Jenkins Documentation Bot"
                        git config user.email "jenkins-docs@localhost"

                        git add docs/html

                        if git diff --cached --quiet; then
                            echo "Documentacion sin cambios"
                        else
                            git commit -m "docs: actualizacion automatica [skip ci]"

                            export GIT_SSH_COMMAND="ssh -i $DOCS_SSH_KEY -o IdentitiesOnly=yes -o StrictHostKeyChecking=yes -o UserKnownHostsFile=/var/jenkins_home/.ssh/known_hosts"

                            git push \
                                git@github.com:hectorlgr/Documentacion_Kali.git \
                                HEAD:main

                            echo "Documentacion subida a GitHub"
                        fi
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Construyendo imagen Docker'

                sh 'docker build -t documentacion-flask-lab:latest .'

                echo 'Iniciando aplicacion Flask'

                sh '''
                    docker rm -f documentacion-flask-lab \
                        >/dev/null 2>&1 || true

                    docker run -d \
                        --name documentacion-flask-lab \
                        --restart unless-stopped \
                        -p 127.0.0.1:5002:5000 \
                        documentacion-flask-lab:latest
                '''

                echo 'Comprobando funcionamiento de Flask'

                sh '''
                    for i in 1 2 3 4 5 6 7 8 9 10; do
                        if docker exec documentacion-flask-lab python -c \
                            "import urllib.request; assert urllib.request.urlopen('http://127.0.0.1:5000/', timeout=3).status == 200"; then
                            echo 'Deploy correcto: HTTP 200'
                            exit 0
                        fi
                        sleep 2
                    done

                    docker logs documentacion-flask-lab
                    exit 1
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'docs/html/**',
                allowEmptyArchive: true,
                fingerprint: true
            )
        }

        success {
            echo 'Pipeline de documentacion completado'
        }

        failure {
            echo 'ALERTA: revisar pipeline de documentacion'
        }
    }
}
