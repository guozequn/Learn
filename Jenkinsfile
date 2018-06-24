pipeline {
  agent any
  stages {
    stage('Stage 1') {
      parallel {
        stage('Check 1') {
          steps {
            sh 'echo check1'
          }
        }
        stage('Check 2') {
          steps {
            sh 'echo Check 2'
          }
        }
        stage('Check 3') {
          steps {
            sh 'echo Check'
          }
        }
      }
    }
    stage('Get Info') {
      steps {
        echo 'What'
      }
    }
  }
}