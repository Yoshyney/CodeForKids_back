pipeline {
    agent {
    docker {
 image 'python:3.7' 
}
 }
    stages {
        stage('Build') {
            steps {
           withEnv(["HOME=${env.WORKSPACE}"]) {
          sh   'export PYTHONPATH=/usr/bin/python:$PYTHONPATH'
          sh  'pip install -r requirements.txt'
          sh 'python hello.py'
            }
        }
    } 
     
        stage('Test') {
            steps {
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
