<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
    <h3 align="center">mario-machine-learning-practice</h3>
    <p align="center">
        슈퍼마리오 게임을 이용한 기계학습 프로젝트
        <br/><br/>
        <a href="https://github.com/koojongin/mario-machine-learning-practice">View Demo</a>
        ·
        <a href="https://github.com/koojongin/mario-machine-learning-practice/issues">Request Feature</a>
    </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#프로젝트에-대해서">About The Project</a>
    </li>
    <li>
      <div>Getting Started</div>
      <ul>
        <li><a href="#Setup--Built-With">Setup & Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#참고자료">References</a>
    </li>
  </ol>
</details>

## 프로젝트에 대해서
평소 데이터 사이언스에 관심이 있었고 직접 해보고 싶다거나 궁금했던 점들이 있었다. 
그래서 기계학습에 대한 개념을 약간 공부하고 이를 이용한 소스코드를 작성해서 직접 구현해보는 것을 목표로 시작한 프로젝트이다.

학습 대상으로는 슈퍼마리오 게임을 선택하였고, 기계학습으로 마리오가 스스로 학습하면서 게임 클리어를 하는 것과 클리어 시간 단축이 최종 목표

## Setup & Built With

```
#1
$ virtualenv .venv
#2
$ virtualenv .venv --python=python3.7
$ source .venv/bin/activate
(.venv) pip install -r requirement.txt 
```

## 참고자료

[강화학습과 MDP(Markov Decision Process)의 개념](http://tcpschool.com/deep2018/deep2018_machine_reinforcement)  
[참고한 예제](https://wonseokjung.github.io/Supermario1/)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/koojongin/mario-machine-learning-practice.svg?style=for-the-badge

[contributors-url]: https://github.com/koojongin/mario-machine-learning-practice/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/koojongin/mario-machine-learning-practice.svg?style=for-the-badge

[forks-url]: https://github.com/koojongin/mario-machine-learning-practice/network/members

[stars-shield]: https://img.shields.io/github/stars/koojongin/mario-machine-learning-practice.svg?style=for-the-badge

[stars-url]: https://github.com/koojongin/mario-machine-learning-practice/stargazers

[issues-shield]: https://img.shields.io/github/issues/koojongin/mario-machine-learning-practice.svg?style=for-the-badge

[issues-url]: https://github.com/koojongin/mario-machine-learning-practice/issues
