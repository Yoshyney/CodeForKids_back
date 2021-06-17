pipeline {
    agent {
    docker {
 image 'python:3.7' 
}
 }
    stages {
        stage('Build') {
            steps {
          sh 'virtualenv testenv -p /usr/bin/python3'
          sh 'source testenv/bin/activate'
            withEnv(["HOME=${env.WORKSPACE}"]) {
          sh  'pip install -r requirements.txt'
                echo 'Building..'
            }
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
