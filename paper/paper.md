---
title: 'AI-ANNE: (A) (N)eural (N)et for (E)xploration'
tags:
  - Explainable Artificial Intelligence
  - MicroPython
  - Microcontroller
  - Embedded Systems
authors:
  - name: Dennis Klinkhammer
    orcid: 0000-0003-1011-5517
    affiliation: 1
affiliations:
 - name: Statistical Thinking (Germany), www.statistical-thinking.de, info (at) statistical-thinking.de
   index: 1
date: 16 March 2025
bibliography: paper.bib
---

# Summary

Machine learning and deep learning are increasingly driving innovation across various fields [@LeCun2015-hn] and can also be transferred on microcontrollers [@Ray2022-oq], for example to process sensor data [@Cioffi2020-lq]. Since microcontrollers have limited computational resources [@Delnevo2023-ux], training or developing neural networks on microcontrollers remains a complex challenge [@Wulfert2024-qf]. However, MicroPython as programming language enables a resource-efficient implementation of neural networks on microcontrollers and provides insights into the fundamentals of neural networks in terms of explainable artificial intelligence [@Haque2023-du; @Meske2022-ke], while coding from scratch in MicroPython also allows for a streamlined and tailored approach [@Delnevo2023-ux]. AI-ANNE: (A) (N)eural (N)et for (E)xploration provides a framework that transfers neural networks from Python to MicroPython and enables the application of pre-trained TensorFlow and Keras models on microcontrollers. Furthermore, it enables users to explore the performance of neural networks while simultaneously the number of neurons and layers as well as the underlying activation functions can be adjusted easily in MicroPython, which makes it also suitable for didactic application [@Collier2024-ld; @Meske2022-ke; @Verma2022-ie; @Scherer2016-fy].

# Statement of need

A previous investigation of skill requirements in artificial intelligence and machine learning job advertisements [Verma2022-ie] served as a guide for the development of AI-ANNE: (A) (N)eural (N)et for (E)xploration. Therefore, it demystifies the mathematical principles underlying neural networks, allowing users to better understand the relationships between data, weights, biases and outputs [@Schmidt2020-ak; @Frank2020-rw; @Scherer2016-fy]. This includes reducing the number of layers, optimizing the activation functions, or using specialized operations to reduce computational load [@Sakr2021-mc]. Moreover, by developing the neural network directly in MicroPython, the model becomes highly portable and adaptable to various microcontroller architectures, such as the Raspberry Pi Pico or the Raspberry Pi Pico 2. Escpecially the step-by-step visibility in MicroPython helps users to identify and understand common challenges like vanishing or exploding gradients, while fostering a more intuitive grasp of how neural networks learn [@Kong2022-sk]. Debugging the code in MicroPython further reinforces this knowledge and provides insights into how errors propagate and are corrected during training. This is in accordance with the primary goals of explainable artificial intelligence [@Haque2023-du; @Schmidt2020-ak] and provides insights into artificial intelligence related responsibilities [@Collier2024-ld; @Frank2020-rw] as well as practical experiences [@Li2021-bn]. As such, implementing neural networks on microcontrollers with AI-ANNE: (A) (N)eural (N)et for (E)xploration shall promote necessary innovation and problem-solving skills [@Verma2022-ie].

# Basic elements
AI-ANNE: (A) (N)eural (N)et for (E)xploration includes the activation functions ReLU, Leaky ReLU, Tanh, Sigmoid and Softmax as pre-installed activation functions. Additional activation functions can be flexibly added in MicroPython. Furthermore, neurons, matrices and matrix transposition as well as the density of neural networks are already pre-programmed in MicroPython. A pre-installed confusion matrix makes it possible to evaluate the performance of different neural networks.

# References
