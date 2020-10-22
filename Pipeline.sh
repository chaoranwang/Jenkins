# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 10:37 上午
# @Author  : Chaorn Wang
# @Email   : chaoran.wcr@dtwave-inc.com
# @File    : Pipeline.py
pipeline{
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}