pipeline {

    agent any

    stages {

        stage('Build Docker Image') {

            steps {

                bat 'docker build -t wine-quality-app .'

            }
        }

        stage('Tag Docker Image') {

            steps {

                bat 'docker tag wine-quality-app aayush296/wine-quality-app'

            }
        }

        stage('Docker Login') {

            steps {

                bat 'docker login -u aayush296'

            }
        }

        stage('Push Docker Image') {

            steps {

                bat 'docker push aayush296/wine-quality-app'

            }
        }

    }

}