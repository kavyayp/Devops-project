pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/kavyayp/Devops-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-app .'
            }
        }

        stage('Run Calculator in Docker') {
            steps {
                echo 'Running calculator inside Docker...'
                sh 'docker run --rm calculator-app'
            }
        }
    }
}
