pipeline {

    agent any

    stages {

        stage('Clone Repository') {

            steps {

                git 'https://github.com/Aayush-Lakhara/wine-quality-project.git'

            }
        }

        stage('Build Docker Image') {

            steps {

                bat 'docker build -t wine-quality-app .'

            }
        }

        stage('Tag Docker Image') {

            steps {

                bat 'docker tag wine-quality-app Aayush-Lakhara/wine-quality-app'

            }
        }

        stage('Push Docker Image') {

            steps {

                bat 'docker push Aayush-Lakhara/wine-quality-app'

            }
        }

    }

}