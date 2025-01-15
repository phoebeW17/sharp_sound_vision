# Sharp Sound & Vision

![ responsive screenshot]

## Introduction

Sharp Sound & Vision (SS&V) is a web application which displays a portfolio of videography projects to attract clients and collaborators. The concept came about when speaking to a friend who wants to start up a film-making business. Existing platforms like social media and traditional portfolios often lack the cohesive and professional presentation needed to stand out in a competitive market. Therefore the site provides my friend with the ability to showcase her work and the feedback she has recieved from fellow collaborators or clients. 

SS&V has been developed as part of the Code Institute's 16 week Full-Stack Developer course as my final individual project - focusing on Django and Bootstrap frameworks, Database manipulation and CRUD functionality.

View live site here : [Sharp Sound & Vision]()  
  
For Admin access with relevant sign-in information: 

<hr>

## Table of Contents

- [Sharp Sound & Vision](#Sharp-Sound-&-Vision)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
- [UX - User Experience](#ux---user-experience)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
    - [Font](#font)
- [Project Planning](#project-planning)
  - [Strategy Plane](#strategy-plane)
    - [Site Goals](#site-goals)
  - [Agile Methodologies - Project Management](#agile-methodologies---project-management)
    - [MoSCoW Prioritization](#moscow-prioritization)
  - [User Stories](#user-stories)
  - [Scope Plane](#scope-plane)
  - [Structural Plane](#structural-plane)
  - [Skeleton \& Surface Planes](#skeleton--surface-planes)
    - [Wireframes](#wireframes)
    - [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
    - [Security](#security)
- [Features](#features)
  - [User View - Registered/Unregistered](#user-view---registeredunregistered)
  - [CRUD Functionality](#crud-functionality)
  - [Feature Showcase](#feature-showcase)
  - [Future Features](#future-features)
- [Technologies \& Languages Used](#technologies--languages-used)
  - [Libraries \& Frameworks](#libraries--frameworks)
  - [Tools \& Programs](#tools--programs)
  - [AI Usage](#ai-usage)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Heroku deployment](#heroku-deployment)
  - [Clone project](#clone-project)
  - [Fork Project](#fork-project)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

  ## Overview

Sharp Sound & Vision is a web application which displays a portfolio of videography projects to attract clients and collaborators. Users and admin are invited to:

- Create or edit content related to the Services and Portfolio pages.
- Register an account to leave a post on the Testimonials page.
- Discover more about the services provided and about the business.

# UX - User Experience

## Design Inspiration

My friend came up with the name Sharp Sound & Vision for her business and as soon as she told me, I had visions of a clean and slick site which has a professional yet unique feel.

I chose to make a mood-board via Pinterest so I could gather inspiration and visuals. Please find the link here: [Pinterest Board](https://pin.it/3HVshY5Uh)


### Colour Scheme

Driven by the inspiration gathered on Pinterest, I found that a neutral set of colours would work best to achieve both a classy and accessible look to the site. In the explore section of [Adobe Color](https://color.adobe.com/search?q=Neutral%20palette&t=term) I found the Palette of Persia. I also tested these with the Adobe Color Contrast Checker.

![screenshot of colour scheme](documentation/images/AdobeColor-Palette%20of%20Persia_%20Brand%20Identity%20for%20Art%20Gallery.jpeg)  
*Colour Scheme for Sharp Sound & Vision website*

![screenshot of the contrast checker](documentation/images/colour%20contrast%20checker.png)
*Colour Scheme Contrast Checker*

![screenshot of the colour blind safe test](documentation/images/COLOUR%20BLIND%20TEST.png)
*Colour Blind Test*

### Font

# Project Planning  
 
## Strategy Plane

### Site Goals

## Agile Methodologies - Project Management

### MoSCoW Prioritization

I chose to follow the MoSCoW Prioritization method for SS&V, identifying and labelling my:

- **Must Haves**: the 'required', critical components of the project. Completing my 'Must Haves' helped me to reach the MVP (Minimum Viable Product) for this project early, allowing me to develop the project further than originally planned.
  
- **Should Haves**: the components that are valuable to the project but not absolutely 'vital' at the MVP stage. The 'Must Haves' must receive priority over the 'Should Haves'.
- **Could Haves**: these are the features that are a 'bonus' to the project, it would be nice to have them in this phase, but only if the most important issues have been completed first and time allows.

## User Stories

User stories and features recorded and managed via a project board on [GitHub Projects](https://github.com/users/phoebeW17/projects/6)

| User Story | Priority |
|----------------------------------------------------------------------------------------------------------------------------|---------------|
| As a **Site User** I would like to **register an account** so that I can **create on a post.** | **MUST HAVE** |
| As a **potential client**, I want to **read testimonials from previous clients** so that I can **gauge the videographer's reliability and professionalism.** | **MUST HAVE** |
| As the **site administrator**, I want to **update the pages on the site**  so that I can **promote and organise my work.** | **MUST HAVE** |
| As a **site user** I want to **navigate the site to find what section I want to access and explore** so that I can **find out more about the site.** | **MUST HAVE** |
| As a **potential client**, I want to **see the services Sharp S&V offers**, so that I can **see what is most appropriate for my project.** | **SHOULD HAVE** |
| As a **returning client**, I want to **see updates and new projects on the website** so that I can **stay informed about the videographer’s recent work.** | **SHOULD HAVE** |
| As a **potential client**, I want to **see an about page**, so that I can **know more about the videographer's professional background and approach to projects.**  | **COULD HAVE** |
| As a **site user** I want to **see the social links and contact details clearly** so that **I can connect to the filmmaker.**  | **COULD HAVE** |


## Scope Plane

## Structural Plane

## Skeleton & Surface Planes

### Wireframes

The wireframes for SS&V were created in Balsamiq. It is useful to quickly create wireframes with it's collection of templates for different devices and viewpoints. It was important to think of how I wanted the site to be viewed on tablets and desktops as well as mobiles so Balsamiq was a good tool to use.

**Mobile/Tablet view for:**  

- About
- Services
- Portfolio
- Testimonials

<details open>
    <summary>Mobile About Page Wireframe</summary>  
    <img src="documentation/wireframes/about mob.png">  
</details>

<details>
    <summary>Tablet About Page Wireframe</summary>  
    <img src="documentation/wireframes/about tab.png">  
</details>

<details>
    <summary>Mobile Services Page Wireframe</summary>  
    <img src="documentation/wireframes/services mob.png">  
</details>

<details>
    <summary>Tablet Services Page Wireframe</summary>  
    <img src="documentation/wireframes/services tab.png">  
</details>

<details>
    <summary>Mobile Portfolio Page Wireframe</summary>  
    <img src="documentation/wireframes/portfolio mob.png">  
</details>

<details>
    <summary>Tablet Portfolio Page Wireframe</summary>  
    <img src="documentation/wireframes/portfolio tab.png">  
</details>

<details>
    <summary>Mobile Testimonials Page Wireframe</summary>  
    <img src="documentation/wireframes/test mob.png">  
</details>

<details>
    <summary>Tablet Testimonials Page Wireframe</summary>  
    <img src="documentation/wireframes/testimonials tab.png">  
</details>
<br>

**Desktop view for:**

- About
- Services
- Portfolio
- Testimonials

<details>
    <summary>Desktop About Page Wireframe</summary>  
    <img src="documentation/wireframes/about desk.png">  
</details>

<details>
    <summary>Desktop Services Page Wireframe</summary>  
    <img src="documentation/wireframes/services desk.png">  
</details>

<details>
    <summary>Desktop Portfolio Page Wireframe</summary>  
    <img src="documentation/wireframes/portfolio desk.png">  
</details>

<details>
    <summary>Desktop Testimonials Page Wireframe</summary>  
    <img src="documentation/wireframes/testimonials desk.png">  
</details>

### Database Schema - Entity Relationship Diagram

### Security

**AllAuth**  

**Defensive Design**  

# Features

## CRUD Functionality

## Feature Showcase 
  
*For features showcase, screenshots of the features in use were taken on Laptop/iPad Air/iPhone X*

## Future Features

# Technologies & Languages Used

- HTML
- CSS
- JavaScript
- Python
- [Git](https://git-scm.com/) used for version control.
- [Github](https://www.github.com) used for online storage of codebase and the Projects tool.
- [Django](https://www.djangoproject.com/) was used as the Python framework for the site.
- [Heroku](https://www.heroku.com) was used to host the SS&V application.


## Libraries & Frameworks

Further information is available in the [requirements.txt file](requirements.txt)

## Tools & Programs

- Adobe Color
- Balsamiq for Wireframes
- Google Fonts
- Pinterest

## AI Usage

#### Tools used: 

I used Microsoft CoPilot in the browser as well as the chat function and pair programmer in VS Code.

#### Example Uses:

 - Use AI tools to assist in
code creation

 - Use AI tools to assist in
debugging code

  <details open>
      <summary>CoPilot Deployment Troubleshooting and Bug Fix</summary>  
      <img src="documentation/images/copilot deploy bug fix.png">  
  </details>



- Use AI tools to optimize
code for performance and user
experience

- Use AI tools to create
automated unit tests

#### Reflection on AI Tools: 

I found the browser version of CoPilot to be useful as it was unobtrusive towards my code project but did have the drawback of not being able to view the sections of code I am working on. However, for the purpose of trouble-shooting I found this most useful.

# Testing

# Deployment
  
## Connecting to GitHub 

## Django Project Setup

## Heroku deployment

## Clone project

## Fork Project

# Credits

- Amy Richardson from Code Institute for the ReadMe structure.

## Code

- Code Institute Learning Materials (Highlighted by comments in project).

## Media

## Acknowledgements

Amy Richardson from Code Institute for her unwavering positivity and support to myself and the bootcamp SY cohort.

Spencer Barriball


