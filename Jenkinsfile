pipeline {
    agent {
    any {
 image 'python:3.7' 
}
 }
    stages {
        stage('Build') {
            steps {
           withEnv(["HOME=${env.WORKSPACE}"]) {
          sh   'export PYTHONPATH=$PATH_TO_MODULE:$PYTHONPATH'
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
