
pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    stages {
        stage('Build') {
            steps {
                sh 'python3 -m compileall -q app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'pipenv sync --dev'
                sh 'pipenv run python -m pytest -q'
            }
        }

        stage('Generate Documentation') {
            steps {
                sh 'doxygen Doxyfile'
                sh 'test -f docs/html/index.html'
            }
        }

        stage('Version Control') {
            steps {
                echo 'Pendiente: configurar escritura en GitHub'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Pendiente: desplegar Flask'
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'docs/html/**',
                allowEmptyArchive: true
            )
        }
    }
}
