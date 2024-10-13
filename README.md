# 2025.djangocon.africa
Website for DjangoCon Africa 2025

## Installation 

To get up and running do the following:


1. Create a virtual environment.

```
python3.12 -m venv venv 
```

Of course there are many ways to make a virtual environment. We are following the simplest method. If you like to use a different thing then go for it.

2. Install the requirements

Activate your virtual env 

```
source venv/bin/activate 
```

Then install the requirements:

```
pip install -r requirements.txt
```

3. Build the tailwind styles 


```
npm install 

npm run tailwind
```

This will create a file called `tailwind_final.css`. This contains the css we use in in our website.

Yo might be tempted to edit `tailwind_final.css` directly at some point. It is an automatically generated file and all changes will be overwritten.

See the "working with Tailwind" section below to learn more.

4. Run the server

Before using the runserver command, you need to load up some environmental variables. `.env_example` has some sensible defaults that just work in a dev environment:

```
source .env_example
python manage.py runserver
```

## Working with tailwind 

You can learn about tailwind [here](https://tailwindcss.com/docs/installation). It is installed in this project using the standard "Tailwind CLI" installation.

The Tailwind CLI is used to build a css file. The build process takes in a few inputs:

1. HTML files: It will look at what tailwind classes you are referencing inside your html files. The final built css file will contain only those css classes that are actually being used. 

2. An input CSS file. In our case we are using `website/static/src/tailwind_input.css`. This file contains any extra classes or default styles.

3. `tailwind.config.js`. This file contains exra configuration. For example if you want to create new colours or define a primary colour or anything like that it will go in there.

The output of the tailwind build is: `website/static/dist/tailwind_final.css`. You can see that we reference this file in our base template, `website/templates/website/_base.html`

### Building the tailwind css file 

There are 2 commands you can use:

This builds the final CSS file:

```
npm run tailwind
```

Sometimes if you are doing a lot of editing of multiple files (html files as well as the other build inputs), then it is useful to watch for file changes and rerun the build automatically.

In this case use:

```
npm run tailwind_watch
```