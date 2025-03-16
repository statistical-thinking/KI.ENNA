---
title: 'Explainable Artificial Intelligence with MicroPython: Lightweight Neural Networks for Students’ Deeper Learning'
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
 - name: FOM University of Applied Sciences, Agrippinawerft 4, 50678 Cologne, Germany
date: 16 March 2025
bibliography: paper.bib
---

### Abstract

> This article contains a scientific tutorial regarding the integration
> of neural networks onto resource-constrained embedded systems like a
> Raspberry Pi Pico / Raspberry Pi Pico 2 as explainable artificial
> intelligence approach for academic teaching and learning settings. It
> shall enable real-time, low-latency, and energy-efficient inference
> while maintaining data privacy, combined with full control by the
> students and detailed insights into artificial intelligence
> fundamentals. Therefore, AI-ANNE: (A) (N)eural (N)et for (E)xploration
> is presented, which facilitates the transfer of pre-trained models
> from high-performance platforms like TensorFlow and Keras onto
> microcontrollers, using a lightweight programming language like
> MicroPython. This approach demonstrates how neural network
> architectures, such as neurons, layers, density and activation
> functions can be implemented in MicroPython in order to deal with the
> computational limitations of embedded systems and for an enhanced
> learning experience. A data classification example will be used as
> intervention in order to contrast this approach to other academic
> teaching and learning setting that make use of TensorFlow and Keras in
> Python. Tukey’s HSD post-hoc test revealed that students who
> implemented neural networks from scratch with MicroPython gained a
> deeper understanding of neural networks than those using TensorFlow
> and Keras, even without the use of microcontrollers.

# (I) Introduction

## Artificial Intelligence on Microcontrollers

Machine Learning and Deep Learning are increasingly driving innovation
across various fields (LeCun et al. 2015), with a notable expansion into
embedded systems, bringing their capabilities closer to data sources.
This trend, known as TinyML, is especially prominent in microcontrollers
and Internet of Things devices. TinyML offers several advantages over
cloud-based artificial intelligence, including improved data privacy,
lower processing latency, energy efficiency, and reduced dependency on
connectivity (Ray 2022). One key application of TinyML is in condition
monitoring, where neural networks can be used to detect anomalies
directly within sensors so that immediate corrective actions can be
taken automatically (Cioffi et al. 2020). Therefore, when these
microcontrollers are connected to microscopes in medical diagnostics or
machines for industrial production, they are referred to as embedded
systems.

While many high-performance frameworks like TensorFlow and Keras for
Python are designed for powerful hardware such as GPUs, these frameworks
are unsuitable for embedded systems due to their limited computational
resources (Delnevo et al. 2023). To address this issue, the architecture
of neural networks need to be reconstructed in a leightweight
programming language like MicroPython. Thus, neural networks trained on
high-performance hardware can be transferred onto resource-constrained
devices like microcontrollers while achieving the same outputs and
results (Ray 2022). However, training or developing neural networks
directly on embedded systems remains a complex challenge. AIfES:
(A)rtificial (I)ntelligence (f)or (E)mbedded (S)ystems, as presented
below as a comparable approach, has shown initial success here (Wulfert
et al. 2024).

This article presents AI-ANNE: (A) (N)eural (N)et for (E)xploration, a
new method for transferring pre-trained neural networks onto a
microcontroller. For this purpose, neurons, layers, density and
activation functions as the underlying foundation of neural networks are
coded in MicroPython in order to be able to reconstruct the original
neural networks trained with TensorFlow and Keras. How the transfer
works and a suitable application example are part of this article. The
underlying foundation of neural networks and their counterparts in
MicroPython are presented successively for an explainable artificial
intelligence approach (Hague et al. 2023; Meske et al. 2022).

Therefore, this article addresses the challenge of implementing neural
networks on microcontrollers while optimizing them for real-time,
resource-constrained environments. The limitations of microcontrollers
make it necessary to carefully consider how neural networks are designed
and executed, while the benefits of coding from scratch in MicroPython
allow for a streamlined, tailored approach (Delnevo et al. 2023). This
balance between resource efficiency and model accuracy will be crucial
in exploring the potential of microcontrollers for more complex and
computationally demanding applications in the future and is intended to
contribute to a better understanding of this technology in the sense of
explainable artificial intelligence and as such for academic teaching
and learning settings.

## Comparable Approach

AIfES: (A)rtificial (I)ntelligence (f)or (E)mbedded (S)ystems is a
flexible software framework designed by Fraunhofer to run deep learning
models on small, low-power devices like microcontrollers (Wulfert et
al. 2024). It simplifies the process of building, training, and running
models directly on these devices, without needing powerful external
systems. Users can customize the framework to fit their needs by
choosing different model components, like types of layers or how data is
processed. AIfES: (A)rtificial (I)ntelligence (f)or (E)mbedded (S)ystems
can run pre-trained models and train new ones on the device itself,
saving energy and protecting privacy (Wulfert et al. 2024). It
outperforms similar tools in terms of speed and memory usage for certain
tasks. Future improvements will focus on making it even more efficient
and supporting new types of deep learning models.

AI-ANNE: (A) (N)eural (N)et for (E)xploration is a similar approach and,
as an open framework, enables the flexible expansion of the underlying
activation functions in order to explore their performance while
simultaneously the number of neurons and layers can be adjusted easily
in MicroPython. This flexibility can also be used for fine-tuning
directly on the microcontroller and for academic teaching and learning
settings. As a result, AI-ANNE: (A) (N)eural (N)et for (E)xploration
allows the learning behavior of the neural networks to be observed and
creates a didactic value for its users. Two neural networks are already
pre-installed: One with six neurons in a total of three layers and one
with eight neurons in a total of four layers. In the intervention
presented within this article, the learning behavior of a neural network
can be investigated with the pre-installed IRIS dataset. The transparent
insight into the MicroPython code also opens up didactic application
potential in terms of explainable artificial intelligence (Collier &
Powell 2024; Scherer 2016). The interaction with the microcontroller
takes place via Thonny. All the necessary components as well as the
purpose of explainable artificial intelligence, as primary goal of this
article, are presented below.

## Research Question

This article deals with the research question of whether students in
academic teaching and learning settings can gain a better understanding
of how neural networks operate by transferring neural networks from
Python to MicroPython while coding directly on microcontrollers.
Therefore, AI-ANNE: (A) (N)eural (N)et for (E)xploration shall not only
contribute in accordance with the explainable artificial intelligence
goals, but should also lead to better results in academic teaching and
learning settings than, for example, when using TensorFlow and Keras in
the Anaconda Cloud. A corresponding evaluation of different academic
teaching and learning settings is therefore the methodological approach
of this article.

## Evaluation of Academic Teaching and Learning Settings

Due to the mentioned limitations of the microcontrollers and the lack of
libraries in MicroPython, a gradual and well-founded introduction to the
functioning of neural networks is required, as provided with AI-ANNE:
(A) (N)eural (N)et for (E)xploration and presented in this article. With
the aim of making a contribution in terms of explainable artificial
intelligence, an evaluation of three different academic teaching and
learning settings is carried out as intervention by using two
consecutive learning assessments as well as the Tukey method (Tukey
1949) for comparison:

-   In the first setting, students learn the basics of neural networks
    in Python and with recourse to TensorFlow and Keras by using
    Anaconda Cloud.

-   In the second setting, students familiarize themselves with neural
    networks in MicroPython and without libraries, but also in the
    Anaconda Cloud.

-   The third setting will be without the Anaconda Cloud and the
    students program the neural networks in MicroPython directly on the
    microcontroller.

The second and third settings will use AI-ANNE: (A) (N)eural (N)et for
(E)xploration, once with and once without the use of a microcontroller.
A subsequent learning progress check enables for an one-way ANOVA based
comparison of the three academic teaching and learning settings, taking
into account the goals of explainable artificial intelligence as stated
in the theoretical background of this article. Therefore, the advantages
and disadvantages of coding neural networks in MicroPython will not only
be highlighted, but shall lead to an improvement of academic teaching
and learning settings as well.

# (II) Theoretical Background

## Explainable Artificial Intelligence

The implementation of neural networks using MicroPython on
microcontrollers can offer substantial educational benefits,
particularly for university students (Meske et al. 2022). By
independently programming the underlying formulas of neural networks,
this approach fosters a transparent understanding of how data flows
through the network, how parameters are adjusted, and how the
architecture and learning processes work (Kong et al. 2022). In this
sense, AI-ANNE: (A) (N)eural (N)et for (E)xploration is a direct
response to the European Year of Skills, that was supposed to empower
people and companies in terms of digital skills for the working world of
the future (Fichtner-Rosada et al. 2024). For this purpose, the
statistical foundations of artificial intelligence were first
systematically compiled and made available as teaching-learning modules
(Klinkhammer & Keller 2024). The elaborated foundations of data science
and analytics by Fayyad and Hamutcu (2020) as well as the investigation
of skill requirements in artificial intelligence and machine learning
job advertisements by Verma et al. (2022) served as a guide for this
compilation and were inspiration for the development of AI-ANNE: (A)
(N)eural (N)et for (E)xploration.

Many students perceive neural networks as complex and opaque due to the
abstraction provided by high-level artificial intelligence libraries
like TensorFlow and Keras. While such tools are essential for practical
applications, they often obscure fundamental concepts (Klinkhammer &
Keller 2024). Implementing neural networks in MicroPython requires
students to explicitly define operations such as matrix multiplications,
activation functions and performance parameters (Kong et al. 2022, Yin
et al. 2019). This hands-on approach demystifies the mathematical
principles underlying neural networks, allowing students to better
understand the relationships between data, weights, biases and outputs
(Schmidt et al. 2020; Scherer 2016). Debugging their code further
reinforces this knowledge and provides insights into how errors
propagate and are corrected during training. This is in accordance with
the primary goals of explainable artificial intelligence (Haque et
al. 2023; Schmidt et al. 2020): trust, transparency, understandability,
usability, and fairness.

Furthermore, microcontrollers, with their limited computational
resources, introduce students to the challenges of optimizing code for
efficiency and performance and could therefore be beneficial in terms of
explainable artificial intelligence as well (Delnevo et al. 2023). By
working within these constraints, students gain a deeper appreciation
for the trade-offs involved in artificial intelligence development,
particularly in the context of embedded systems and edge devices. This
practical experience may close the gap between theoretical knowledge and
real-world applications (Collier & Powell 2024; Li et al. 2021).
Additionally, students can log and analyze intermediate results, such as
hidden layer outputs and weight updates, providing a transparent view of
the network’s learning process (Frank et al. 2020). This step-by-step
visibility helps to identify and understand common challenges like
vanishing or exploding gradients, fostering a more intuitive grasp of
how neural networks learn (Kong et al. 2022).

Implementing neural networks independently also encourages innovation
and problem-solving (Fayyad & Hamutcu 2020). Students must manage
trade-offs between model complexity and hardware limitations, design
minimalistic yet functional architectures, and experiment with
lightweight alternatives to traditional methods. These challenges
require critical thinking and creativity, valuable skills in the
evolving atificial intelligence landscape (Verma et al. 2022). Moreover,
working with microcontrollers makes artificial intelligence education
more accessible, as these devices are inexpensive and widely available,
lowering barriers for students and institutions with limited resources.

This transparent implementation approach also provides a platform for
discussing ethical considerations in artificial intelligence. Students
can explore how biases in training data influence model behavior, the
implications of design choices on fairness and interpretability, and the
importance of building explainable and accountable systems. These
discussions cultivate a deeper awareness of the societal impact of
artificial intelligence and the responsibility of artificial
intelligence practitioners (Collier & Powell 2024; Frank et al. 2020).

## Obstacles of Microcontrollers as Didactical Value

Microcontrollers, while offering an array of advantages in embedded
systems, come with significant limitations that impact the deployment of
computationally intensive models like neural networks (Ray 2022). Their
restricted memory capacity, processing power, and limited support for
advanced libraries can pose challenges in real-time applications
(Delnevo et al. 2023). These constraints can result in slower inference
times, higher energy consumption, and a reduction in the overall model
performance, especially when compared to high-powered systems running
frameworks like TensorFlow and Keras. Furthermore, microcontrollers lack
the ability to handle large-scale floating-point operations efficiently,
which are typically used in neural network computations (Ray 2022). As
such, models need to be carefully designed to fit within these
limitations, avoiding resource-hungry operations that would otherwise
lead to failure or excessive power consumption. This makes running deep
neural networks that require multiple layers and complex activations
particularly challenging on microcontroller platforms (Delnevo et
al. 2023).

Despite these limitations, there are distinct advantages to coding
neural networks from scratch in MicroPython for microcontroller
deployment. The primary benefit lies in full control over the network’s
architecture and computation, allowing for significant customizations
that align closely with the constraints of the microcontroller. Writing
the network from scratch, rather than relying on a prebuilt framework,
offers the flexibility to tailor the implementation to specific needs
(Kong et al. 2022), which could align with the explainable artificial
intelligence goals (Haque et al. 2023; Schmidt et al. 2020). This
includes reducing the number of layers, optimizing the activation
functions, or using specialized operations to reduce computational load
(Sakr et al. 2021). Moreover, by developing the neural network directly
in MicroPython, the model becomes highly portable and adaptable to
various microcontroller architectures, such as the Raspberry Pi Pico or
the Raspberry Pi Pico 2, and allow for an hands-on experience with
artificial intelligence.

## Specifications of the Raspberry Pi Pico / Raspberry Pi Pico 2

The Raspberry Pi Pico is powered by the RP2040 microcontroller, which
features a dual-core ARM Cortex-M0+ processor running at 133 MHz, with
264 KB on-chip SRAM and 2 MB onboard flash memory. It offers a wide
range of connectivity options, including USB for power and data
transfer, up to two I2C, SPI, and UART interfaces for communication, as
well as 16 PWM channels for precise control of external devices.

The board also includes three 12-bit ADC channels for analog input, and
it supports a range of peripherals such as a real-time clock (RTC),
timers, and interrupt handling through a nested vectored interrupt
controller (NVIC). For power, the Raspberry Pi Pico operates on a
voltage range of 1.8V to 3.6V, with typical consumption between 20-100
mA, and can be powered via the micro-USB port or the VSYS pin for
external power sources like batteries or regulated supplies.

In 2024 an updated Raspberry Pi Pico 2 was introduced, which is powered
by the RP2350 microcontroller, which features a dual-core ARM Cortex-M33
processor running at 150MHz and 520 KB on-chip SRAM and 4 MB onboard
flash memory. Both can be operated with MicroPython. It can be assumed
that the Raspberry Pi Pico 2 can calculate larger datasets and more
complex neural networks with AI-ANNE: (A) (N)eural (N)et for
(E)xploration. Therefore, the use of a Raspberry Pi Pico 2 is
recommended for practical use; The use of the Raspberry Pi Pico might be
sufficient for educational purpose.

## MicroPython Coding on Microcontrollers with Thonny

MicroPython is an efficient, lightweight implementation of the Python
programming language designed to run on microcontrollers and embedded
systems with constrained resources (Delnevo et al. 2023). Unlike the
full Python environment, MicroPython is optimized to operate within the
memory and processing limits typical of small-scale devices, offering a
streamlined interpreter and a subset of Python’s standard libraries.
MicroPython retains much of Python’s high-level syntax and ease of use,
making it accessible to developers familiar with Python. It is
particularly well-suited for rapid prototyping, development, and
deployment of machine learning and neural network models on embedded
platforms, where resources such as memory, computational power, and
storage are limited.

In the context of neural network applications, MicroPython is often used
in edge computing scenarios, where deep learning models need to be
deployed directly onto microcontroller-based systems for real-time,
localized inference. Although MicroPython does not natively support the
extensive numerical libraries found in full Python (e.g., TensorFlow and
Keras), it is possible to reproduce the basic architecture of neural
networks with AI-ANNE: (A) (N)eural (N)et for (E)xploration in
MicroPython from scratch.

Thonny is a simple, user-friendly program that works on all major
computer systems. It makes it easy to connect with and program the
Raspberry Pi Pico / Raspberry Pi Pico 2. Thonny enables users to quickly
write and test code, manage files and fix any mistakes with helpful
tools. It can be described as a tool for those just starting with
MicroPython on microcontrollers and embedded systems. With Thonny,
AI-ANNE: (A) (N)eural (N)et for (E)xploration can simply be flashed onto
the microcontroller.

# (III) Implementing Neural Networks in MicroPython

## Architecture of Neural Networks

A neural network is a computational model inspired by the way biological
neural systems process information. It consists of interconnected layers
of nodes, or neurons, which transform input data into output predictions
through a series of mathematical operations (LeCun et al. 2015). In the
context of implementing neural networks in MicroPython, the architecture
must be designed to operate within the resource constraints of embedded
systems (Ray 2022). Despite these constraints, the basic components of a
neural network - neurons, layers, density, and activation functions -
can still be effectively modeled (Sakr et al. 2021).

### a) Neurons

A neuron in a neural network is a computational unit that receives
inputs, applies a weight to each input, sums the weighted inputs, and
passes the result through an activation function to produce an output.
In MicroPython (Appendix - C), each neuron can be represented as a
mathematical operation involving inputs and weights, with the output
being calculated via simple matrix operations.

The general form of the neuron’s computation can be expressed with *y*
as the output of the neuron, *f* as the activation function,
*x*<sub>*i*</sub> as the inputs, *w*<sub>*i*</sub> as the corresponding
weights and *b* as the bias:

*y* = *f*(∑<sub>*i*</sub>*w*<sub>*i*</sub>*x*<sub>*i*</sub>+*b*)

In a MicroPython implementation, these calculations can be done using
basic array operations, making it computationally efficient for
small-scale neural networks on microcontrollers.

### b) Layers

A neural network is typically structured as a series of layers, where
each layer consists of multiple neurons. There are three main types of
layers in a typical neural network architecture:

-   Input Layer: This is the first layer of the network and receives the
    raw input data. Each neuron in the input layer corresponds to a
    feature in the input data. With AI-ANNE: (A) (N)eural (N)et for
    (E)xploration, this layer would typically read sensor values or
    external data directly.

-   Hidden Layers: Between the input and output layers, the network may
    contain one or more hidden layers. These layers are responsible for
    learning complex representations of the input data. Each hidden
    layer is composed of neurons that perform weighted sums of the
    outputs of the previous layer, followed by an activation function.

-   Output Layer: This is the final layer of the network, which produces
    the prediction or classification result. The output layer’s
    structure depends on the problem being solved (e.g., binary
    classification, multi-class classification, logistic regression).

MicroPython can represent the layers as a list of lists (or arrays) of
neurons, where each element stores the weights, biases, and outputs of
the neurons in the respective layer.

### c) Density

The density of a layer refers to the number of neurons in that layer. In
a fully connected (dense) layer, each neuron in the current layer is
connected to all neurons in the previous layer. This is the most common
configuration in neural networks. For example: In a dense layer with 5
neurons, each neuron in the layer receives input from all neurons in the
previous layer, and the layer will contain 5 sets of weights and biases
to be learned during training. MicroPython can implement a dense layer
efficiently using matrix multiplication (Appendix - A, all of a sudden,
school math seems very practical!). Each layer’s input and weight
matrices are multiplied together, followed by the addition of a bias
term, and the result is passed through an activation function.

### d) Activation Functions

An activation function determines whether a neuron should activate, so
that the neuron’s output will be passed forward to the next layer. The
activation function introduces non-linearity into the network, allowing
it to learn complex patterns in the data. Common activation functions
include:

-   Sigmoid: The Sigmoid function outputs values between 0 and 1 and is
    often used in binary classification tasks.

$$Sigmoid(x) = \frac{1}{1 + e^{-x}}$$

-   ReLU (Rectified Linear Unit): ReLU outputs the input directly if it
    is positive; otherwise, it outputs zero. It is widely used in hidden
    layers due to its simplicity and efficiency in preventing vanishing
    gradients.

$${ReLU}(x) = 
\begin{cases} 
x & \text{if } x \geq 0 \\
0 & \text{if } x &lt; 0 
\end{cases}$$

-   Leaky ReLU: The Leaky ReLU activation function is a variant of the
    traditional ReLU activation function, which addresses a common issue
    known as the “dying ReLU” problem. This problem occurs when neurons
    become inactive and stop learning because their output is always
    zero (when the input is negative). Leaky ReLU overcomes this by
    allowing a small, non-zero gradient when the input is negative. The
    key difference between ReLU and Leaky ReLU is that when *x* &lt; 0,
    instead of the output being zero (as in ReLU), the output is a small
    negative value. The parameter *a**l**p**h**a* controls the slope of
    this negative region, typically with small values such as 0.01 or
    0.1.

$${Leaky ReLU}(x) = 
\begin{cases} 
x & \text{if } x \geq 0 \\
\alpha x & \text{if } x &lt; 0 
\end{cases}$$

-   Tanh: The hyperbolic tangent function Tanh outputs values between -1
    and 1. It is similar to the sigmoid but has a wider output range,
    making it useful for some applications where the network needs to
    model both positive and negative values.

$$Tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

-   Softmax: Often used in the output layer of classification networks,
    the Softmax function normalizes the output to produce a probability
    distribution across multiple classes.

$${Softmax}(x\_i) = \frac{e^{x\_i}}{\sum\_{j} e^{x\_j}}$$

In MicroPython, these activation functions can be implemented as simple
functions, leveraging MicroPython’s built-in math library (Appendix -
B). Given the computational constraints of embedded devices, it is
crucial to choose lightweight activation functions like ReLU, which
avoid the more computationally expensive exponentiation operations used
in Sigmoid or Tanh. AI-ANNE: (A) (N)eural (N)et for (E)xploration passes
data through the neural network layer by layer, and each neuron’s output
is computed based on the inputs and weights. In a MicroPython
environment, due to the limited processing power and memory, a smaller
network with fewer layers and neurons might be preferred, and training
could be done in advance on a more powerful system before deployment to
the embedded device.

### e) Weights and Biases

In neural networks, weights and biases are key parameters that the model
learns during the training process to make accurate predictions.

Weights are the parameters that scale the input values as they pass
through the network. They determine the strength of the connections
between neurons in adjacent layers. Each connection between two neurons
has its own weight, and the value of this weight influences how much the
input from the previous layer affects the output of the current layer.
In mathematical terms, if a neuron receives an input *x* and its
corresponding weight is *w*, the contribution of that input to the
neuron’s output is *w* \* *x*. Weights are adjusted during training
using optimization techniques, such as gradient descent, to minimize the
model’s prediction error.

Biases, on the other hand, allow the model to shift the output
independently of the weighted sum of inputs. They are added to the
weighted sum before it is passed through the activation function. This
allows the network to better model complex relationships in the data by
shifting the activation function’s threshold. For example, if the
weighted sum of inputs to a neuron is represented as
*z* = *w* \* *x* + *b*, the bias term *b* shifts the output, enabling
the model to learn more effectively. Like the weights, biases are also
learned during training.

# (IV) Research Method

## Sample Description

Considering the goals of explainable artificial intelligence, which are
trust, transparency, understandability, usability, and fairness, an
evaluation of three different academic teaching and learning settings is
carried out: A total of 144 students were randomly divided into three
groups, so that each group contained a total of 48 students. The
students were first-year students and their prior knowledge of how
neural networks work was comparably low across all groups. Each group
was confronted with a different academic teaching and learning setting
as intervention and two learning assessment - one before and one after
the intervention, which were conducted within three consecutive hours.
The initial learning assessment was based on twenty questions (that
accordingly resulted in a 20-point scale in which each correctly
answered question yielded one point) on basic definitions and principles
of neural networks as well as their interpretation and the groups scored
initially as follows, showing no significant differences (Tab. 1):

### (Tab. 1) Mean-Score and Standard Deviation before Intervention

<table class="table" style="margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
</th>
<th style="text-align:center;">
Group 1
</th>
<th style="text-align:center;">
Group 2
</th>
<th style="text-align:center;">
Group 3
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
Mean-Score (SD)
</td>
<td style="text-align:center;">
02.54 (01.16)
</td>
<td style="text-align:center;">
02.62 (01.19)
</td>
<td style="text-align:center;">
02.50 (01.23)
</td>
</tr>
</tbody>
</table>

## Intervention: A Binary Classsification Task

All groups were confronted with a binary classification task, based upon
the IRIS dataset. The IRIS dataset is a widely recognized dataset in
statistics, machine learning and deep learning and often used for
classification problems. Introduced by the British biologist and
statistician Fisher (1936), it contains 150 instances of iris flowers,
each with four attributes that describe their physical characteristics.
These attributes include the sepal length, sepal width, petal length,
and petal width, all measured in centimeters.

Based on these four attributes, the objective of the dataset is to
classify each flower into one of three species: Setosa, Versicolor, and
Virginica. The IRIS dataset serves as an ideal example for demonstrating
and testing machine learning algorithms and neural networks as deep
learning models, particularly for classification tasks. Its manageable
size, clear distinctions between classes and straightforward nature make
it a popular choice for exploring classification techniques. However,
classifying some of the species, particularly Versicolor and Virginica,
can be challenging due to their overlapping characteristics, making the
task more complex for certain machine learning algorithms and neural
networks as deep learning models.

Group 1 performed the classification task with two different neural
networks in Python and with recourse to TensorFlow and Keras by using
Anaconda Cloud, while Group 2 performed the same classifcation task in
the Anaconda Cloud, but without recourse to TensorFlow and Keras.
Therefore, Group 2 made use of the MicroPyton code of AI-ANNE: (A)
(N)eural (N)et for (E)xploration. Finally, Group 3 used the MicroPyton
code of AI-ANNE: (A) (N)eural (N)et for (E)xploration only via Thonny
and directly on the microcontroller. The architecture and performance of
the neural networks did not differ, only the programming language and
the additional use of a microcontroller.

## Expected Benefits of Implementing Neural Networks in MicroPython

In addition to the mathematical basics (Appendix - A), that need to be
coded in MicroPython, insights into the activation functions of neural
networks (Appendix - B) and neurons (Appendix -C) are provided with
AI-ANNE: (A) (N)eural (N)et for (E)xploration. Applying these
fundamentals in TensorFlow and Keras would make the implementation of
neural networks fast, but without further insights into the underlying
formulas and the corresponding code. In order to run neural networks
with AI-ANNE: (A) (N)eural (N)et for (E)xploration and on
microcontrollers, students need to follow a certain procedure, which
could make artificial intelligence more explainable:

First, with TensorFlow and Keras pre-trained weights and biases must be
transferred onto the microcontroller. Groups 2 and 3 were provided with
the weights and biases so that they could focus on the actual
architecture of the neural networks in MicroPython. The weights and
biases of the neural network with 8 neurons need to be coded in a
specific order in MicroPython (Tab. 2). This process is illustrated
below by exampling one of the neural network of the intervention. The
first layer contains two neurons that process the input from the four
independent variables of the IRIS dataset. The weights *w*1 are coded
accordingly with two columns and four rows in MicroPython. The two
neurons are correspondingly provided with two biases *b*1. The weights
and biases for the number of neurons in the other layers are coded
accordingly: Three neurons follow in a hidden layer, followed by two
neurons in another hidden layer and one neuron in the output layer.

### (Tab. 2) Weights and Biases for 8 Neurons

          w1 = [[-0.75323504, -0.25906014],
                [-0.46379513, -0.5019245 ],
                [ 2.1273055 ,  1.7724446 ],
                [ 1.1853403 ,  0.88468695]]
          b1 = [0.53405946, 0.32578036]
          w2 = [[-1.6785783,  2.0158117,  1.2769054],
                [-1.4055765,  0.6828738,  1.5902631]]
          b2 = [ 1.18362  , -1.1555661, -1.0966455]
          w3 = [[ 0.729278  , -1.0240695 ],
                [-0.80972326,  1.4383037 ],
                [-0.90892404,  1.6760625 ]]
          b3 = [0.10695826, 0.01635581]
          w4 = [[-0.2019448],
                [ 1.5772797]]
          b4 = [-1.2177287]

For pre-training in TensorFlow and Keras the ReLU activation function
was used in the input layer, followed by Tanh in the first hidden layer,
Softmax in the second hidden layer and Sigmoid in the output layer. This
MicroPython code is quite similar to the way of programming with
TensorFlow and Keras, except that the underlying activation functions
had to be programmed manually (Appendix - B). In MicroPython (Tab. 3),
where students have the option to change the number of neurons, layers
as well as changing the activation functions used, the corresponding
code would be:

### (Tab. 3) Neural Network with 8 Neurons

          yout1 = dense(2, transpose(Xtest), w1, b1, 'relu')
          yout2 = dense(3, yout1, w2, b2, 'tanh')
          yout3 = dense(2, yout2, w3, b3, 'softmax')
          ypred = dense(1, yout3, w4, b4,'sigmoid')

The accuracy of this neural network with 8 neurons is 90%. A variation
of the number of neurons, layers as well as activation functions with
their weights and biases can influence the accuracy accordingly.
Therefore, AI-ANNE: (A) (N)eural (N)et for (E)xploration enables direct
customization of the code in MicroPython, either on the Anaconda Cloud
or via Thonny for microcontrollers, and comes with two preinstalled
neural networks. The second neural network is based upon 6 neurons and
results in an accuracy of 95%, whereby flexible adjustments are also
possible. The different accuracies demonstrate the importance of the
number of neurons and layers as well as the activation functions used.
In this case, a simpler neural network seems to be more appropriate. In
summary, the main difference to TensorFlow and Keras lies in the
completely manual programming method and the transparent display of all
functions.

# (V) Results

## Didactical Assessment

The didactical assassment is based upon another run of the learning
assessment with slightly different questions and Tukey’s HSD, the
Honestly Significant Difference post-hoc test (Tukey 1949), in order to
indicate which groups were significantly different from another (Tab.
4). As one-way ANOVA it is similar in interpretation to the unpaired
Student’s t-test who would be limited to the comparison of two groups.
First of all, it should be noted that all groups experienced a
significant increase within the second learning assessment and probably
as a result of the intervention. However, the main differences become
apparent when the groups are compared with each other:

### (Tab. 4) Mean-Score and Standard Deviation after Intervention

<table class="table" style="margin-left: auto; margin-right: auto;">
<thead>
<tr>
<th style="text-align:center;">
</th>
<th style="text-align:center;">
Group 1
</th>
<th style="text-align:center;">
Group 2
</th>
<th style="text-align:center;">
Group 3
</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align:center;">
Mean-Score (SD)
</td>
<td style="text-align:center;">
13.27 (02.35)
</td>
<td style="text-align:center;">
15.37 (02.38)
</td>
<td style="text-align:center;">
16.12 (02.33)
</td>
</tr>
</tbody>
</table>

Based on the three groups, each with a different intervention, the
following findings can be derivated: The difference between Group 1 and
Group 2, according to Tukey’s HSD post-test, is 02.10 (95% CI: 00.96 to
03.23) and signifiant (p=.0001). Furthermore, the difference between
Group 1 and 3 is 02.85 (95% CI: 01.71 to 03.98) and also significant
(p=.000). However, the difference between Group 2 and Group 3 is only
00.75 (95% CI: -00.38 to 01.88) and not significant (p=.2659). From this
it can be deduced that programming a neural network in MicroPython
contributes more to understanding the underlying functionality than an
approach with TensorFlow and Keras in the Anaconda Cloud. The use of an
additional microcontroller and its programming using Thonny therefore
does not contribute to a better understanding of how neural networks
work. However, it should be noted that the students were confronted with
two predefined neural networks as part of the intervention, which did
not exhaust the limitations of the microcontroller.

## Technological Assessment

The presented neural networks have been specifically optimized for
deployment on microcontrollers by directly implementing the core
functions in MicroPython, which significantly reduces the memory and
computational overhead compared to using external machine learning
libraries like TensorFlow. This custom approach ensures that the model
can run efficiently on microcontrollers with limited resources. The
activation functions, such as ReLU, Leaky ReLU, Tanh, Sigmoid, and
Softmax, are manually coded using basic MicroPython operations. These
simple, efficient functions avoid the complexity of more
resource-intensive methods, ensuring that the network’s execution
remains lightweight. Additionally, fundamental matrix operations like
addition, transposition, and zero-initialization are implemented in
MicroPython without the need for external dependencies, further
minimizing the model’s memory footprint.

This design choice prioritizes flexibility and scalability, allowing the
neural networks to be easily adapted to different microcontroller
platforms. The custom functions are optimized for real-time inference,
focusing on basic loop-based operations and element-wise calculations,
which are suitable for devices with limited processing power and memory.
The model can thus process data quickly and provide predictions with
minimal delay, making it appropriate for embedded applications where
real-time decision-making is critical. This approach ensures that the
neural network can operate efficiently even on microcontrollers with
constraints, allowing for seamless integration into embedded systems for
classification tasks like the IRIS dataset. The lightweight design also
ensures that the model can be executed on low-power devices, essential
for battery-powered or remote applications.

In a further development process, it should be possible to dispense with
the parameters of pre-trained models and train directly on the
microcontroller, which would require calculating gradients and updating
weights via backpropagation as well as the implementation of appropriate
loss functions. It remains to be seen to what extent the
microcontrollers are capable of carrying out these calculation steps.

# (VI) Discussion

This article explored the integration of neural networks onto
resource-limited microcontrollers and embedded systems like the
Raspberry Pi Pico and Raspberry Pi Pico 2 for academic teaching and
learning settings. This method enabled the deployment of neural networks
directly on microcontrollers, providing real-time, low-latency, and
energy-efficient inference while ensuring data privacy. For this
purpose, AI-ANNE: (A) (N)eural (N)et for (E)xploration was introduced, a
open source framework that facilitated the transfer of pre-trained
models from high-performance platforms like TensorFlow and Keras to
microcontrollers, using MicroPython as lightweight and transparent
programming languages. The approach demonstrated how key neural network
components — such as neurons, layers, density, and activation functions
— could be implemented in MicroPython in order to address the
computational constraints of microcontrollers and embedded systems.
These neural networks achieve exactly the same results on the
microcontroller as the computationally intensive models with TensorFlow
and Keras.

However, the primary goal of this approach is to make a contribution in
terms of explainable artificial intelligence, based upon trust,
transparency, understandability, usability, and fairness of artificial
intelligence. By implementing neural networks in MicroPython, students
were supposed to gain a robust understanding of artificial intelligence
principles, develop practical skills, and learn to innovate within
constraints. This method transforms artificial intelligence education
into an interactive and transparent process, preparing students not only
for advanced research and professional applications but also to become
responsible and effective contributors to the field.

Therefore, this article examined the impact of different teaching and
learning settings on students’ understanding of neural networks,
considering key aspects of explainable artificial intelligence. While
all groups experienced significant learning gains through academic
teaching and learning settings as intervention, key differences emerged
when comparing the groups that implemented neural networks using
different methodological approaches. Statistical analysis using Tukey’s
HSD post-hoc test revealed that students who implemented neural networks
with TensorFlow and Keras in Python performed significantly worse than
those who programmed the same model in MicroPython from scratch. An even
larger difference was observed between those using TensorFlow and Keras
and the group that executed the MicroPython implementation directly on a
microcontroller. As long as the students used MicroPython, the
difference was not statistically significant. This suggests that
implementing neural networks in MicroPython, regardless of whether a
microcontroller is used, leads to a better understanding of how neural
networks function compared to using TensorFlow and Keras. However, it is
important to note that the intervention was limited to two predefined
neural networks and did not fully explore the limitations of
microcontrollers. Future studies should investigate whether further
implementation and optimization of neural networks on microcontrollers
contribute to an even deeper understanding.

# (VII) Conclusion

AI-ANNE: (A) (N)eural (N)et for (E)xploration, a open source framework,
demonstrated how key neural network components — such as neurons,
layers, density, and activation functions — could be implemented in
MicroPython. It can not only be used to enable a cost-effective and
transparent implementation of neural networks on microcontrollers, but
to provide insights into the fundamentals of artificial intelligence as
well, for which it was honored with the award for excellent teaching in
2024 and the research award in 2025 at the FOM University of Applied
Sciences in Germany. Therefore, this article was created to
transparently disclose the underlying methodology by offering a simple
and practical method for deploying neural networks on energy-efficient
devices like microcontrollers and how they can be used for practical use
or as an educational tool with insights. AI-ANNE: (A) (N)eural (N)et for
(E)xploration and all presented codes are an open source project and can
be used by anyone in accordance with the terms of the German Free
Software License (Appendix - D). In particular, the use of MicroPython
and the manual programming of the basics of neural networks has proven
to be very promising in terms of explainable artificial intelligence. As
a result, the following implications shall conclude this article and
inspire further work in terms of explainable artificial intelligence and
its goals:

-   Trust and Transparency: The lower learning outcomes associated with
    using TensorFlow and Keras suggest that the high level of
    abstraction in these frameworks makes it harder to grasp model
    architectures and learning processes. Direct implementation in
    MicroPython provides deeper insight into neural network
    functionality.

-   Understandability: The superior performance of students using
    MicroPython highlights that an educational approach requiring
    explicit implementation fosters a deeper understanding of
    fundamental concepts.

-   Usability and Fairness: While TensorFlow and Keras offer ease of
    use, they may hinder students with less programming experience from
    fully understanding key principles. A balanced educational approach
    should consider both efficiency and comprehension.

# About the Author

-   Dennis Klinkhammer completed his doctorate and habilitation at
    Justus Liebig University Giessen (JLU) and got an award for
    excellent teaching as well as the research award for his didactical
    insights into the methodological foundations of machine learning and
    deep learning in the programming languages R and Python at FOM
    University of Applied Sciences in Germany. Making artificial
    intelligence explainable is the main focus of his academic teaching
    and research.

# Open Source Code

-   Both the presented and other examples of AI-ANNE: (A) (N)eural (N)et
    for (E)xploration are available on GitHub and online:
    <https://www.statistical-thinking.de/ai-anne.html>. This includes
    Jupyter Notebooks for pre-training with TensorFlow and Keras in
    Python, as well as the parameters to be transferred and the
    corresponding code in MicroPython. The link to the repository is:
    <https://github.com/statistical-thinking/KI.ENNA>

# Appendices

## (A) Mathematical Basics in MicroPython

These mathematical basics enable matrix multiplication and other
important operations for the neural network architecture. The codes
(Tab. A) therefore do not need to be adapted in MicroPython!

### (Tab. A) Mathematical Basics

          # Mathematical Basics - I
          def zero_dim(x):
              z = [0 for i in range(len(x))]
              return z
          
          # Mathematical Basics - II
          def add_dim(x, y):
              z = [x[i] + y[i] for i in range(len(x))]
              return z
          
          # Mathematical Basics - III
          def zeros(rows, cols):
              M = []
              while len(M) < rows:
                  M.append([])
                  while len(M[-1]) < cols:
                      M[-1].append(0.0)
              return M
          
          # Mathematical Basics - IV
          def transpose(M):
              if not isinstance(M[0], list):
                  M = [M]
              rows = len(M)
              cols = len(M[0])
              MT = zeros(cols, rows)
              for i in range(rows):
                  for j in range(cols):
                      MT[j][i] = M[i][j]
              return MT
          
          # Mathematical Basics - V
          def print_matrix(M, decimals=3):
              for row in M:
                  print([round(x, decimals) + 0 for x in row])
          
          # Mathematical Basics - VI
          def dense(nunit, x, w, b, activation):
              res = []
              for i in range(nunit):
                  z = neuron(x, w[i], b[i], activation)
                  res.append(z)
              return res

## (B) Activation Funtions in MicroPython

The following code (Tab. B) demonstrates how the activation functions
Sigmoid, ReLU, Leaky ReLU, Tanh and Softmax can be programmed in
MicroPython. In TensorFlow and Keras these are already pre-programmed,
in MicroPython the programming has to be done manually. Additional
activation functions can be added accordingly.

### (Tab. B) Activation Functions

          # Sigmoid
          def sigmoid(x):
              z = [1 / (1 + math.exp(-x[val])) for val in range(len(x))]
              return z
            
          # ReLU
          def relu(x):
              y = []
              for i in range(len(x)):
                  if x[i] >= 0:
                      y.append(x[i])
                  else:
                      y.append(0)
              return y
          
          # Leaky ReLU
          def leaky_relu(x, alpha=0.01):
              p = []
              for i in range(len(x)):
                  if x[i] >= 0:
                      p.append(x[i])
                  else:
                      p.append(alpha * x[i])
              return p
          
          # Tanh
          def tanh(x):
              t = [(math.exp(x[val]) - math.exp(-x[val])) / (math.exp(x[val])
                + math.exp(-x[val])) for val in range(len(x))]
              return t
          
          # Softmax
          def softmax(x):
              max_x = max(x[val])
              exp_x = [math.exp(val - max_x) for val in range(len(x))]
              sum_exp_x = sum(exp_x)
              s = [j / sum_exp_x for j in exp_x]
              return s

## (C) Neurons in MicroPython

The predefined activation functions Sigmoid, ReLU, Leaky ReLU, Tanh and
Softmax are already pre-programmed for each neuron in MicroPython (Tab.
C). Activation functions that are added independently must be added
accordingly.

### (Tab. C) Neurons

          # Single Neuron
          def neuron(x, w, b, activation):
          
              tmp = zero_dim(x[0])
          
              for i in range(len(x)):
                  tmp = add_dim(tmp, [(float(w[i]) * float(x[i][j]))
                    for j in range(len(x[0]))])
          
              if activation == "sigmoid":
                  yp = sigmoid([tmp[i] + b for i in range(len(tmp))])
              elif activation == "relu":
                  yp = relu([tmp[i] + b for i in range(len(tmp))])
              elif activation == "leaky_relu":
                  yp = relu([tmp[i] + b for i in range(len(tmp))])
              elif activation == "tanh":
                  yp = tanh([tmp[i] + b for i in range(len(tmp))])
              elif activation == "softmax":
                  yp = tanh([tmp[i] + b for i in range(len(tmp))])
              else:
                  print("Function unknown!")
          
              return yp

## (D) German Free Software License

AI-ANNE: (A) (N)eural (N)et for (E)xploration and KI-ENNA: (E)in
(N)euronales (N)etz zum (A)usprobieren may be used by anyone in
accordance with the terms of the German Free Software License. The
German Free Software License (Deutsche Freie Software Lizenz) is a
license of open-source nature with the same flavors as the GNU GPL but
governed by German law. This makes the license easily acceptable to
German authorities. The D-FSL is available in German and in English.
Both versions are equally binding and are available at:
<http://www.d-fsl.org/>

# References