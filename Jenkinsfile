pipeline {
    agent {
    docker {
 image 'python:3-alpine' 
}
 }
    stages {
        stage('Build') {
            steps {
            sh ' sudo pip install -r requirements.txt'
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
            sh 'python hello.py'
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
