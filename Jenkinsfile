pipeline {
    agent any

    environment {
        // Points to the secret file we created on Instance B
        ENV_FILE = '/var/lib/jenkins/secrets/techsol.env'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls code from your GitHub repo
                checkout scm
            }
        }

        stage('Build & Deploy') {
            steps {
                script {
                    // Runs docker-compose using your specific pipeline file and secret env
                    sh "docker compose -f docker-compose.pipeline.yml --env-file ${ENV_FILE} up -d --build"
                }
            }
        }

        stage('Cleanup') {
            steps {
                // Removes old unused images to save that precious disk space
                sh 'docker image prune -f'
            }
        }
    }
}
