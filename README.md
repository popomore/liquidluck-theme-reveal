# Reveal.js theme for Liquidluck

It will help you to generate ppt from markdown.

Thanks [reveal.js](https://github.com/hakimel/reveal.js) and [liquidluck](https://github.com/lepture/liquidluck).

## How

### Install liquidluck and theme

```
$ pip install liquidluck -g
$ liquidluck install reveal -g
```

### init

You can choose your post folder and output folder.

```
$ liquidluck init                                                                                                                                                
Select a config format ([yaml], python, json):  json
posts folder (content): content
output folder (deploy): ppt
```

### Configuration

```
"theme": {
    "name": "reveal",
    "vars": {
    }
  },
```

### Write PPT

```
$ cd content
$ touch example.md
```

open and edit example.md

    # Example
    
    - date: 2012-01-01
    
    ---
    
    # Slide one
    
    - list1
    - list2
    
    ---
    
    # Slide two
    
    paragragh

each slides splits by `---`

### build and deploy

```
$ liquidluck build
$ liquidluck server
```

Then push to gh-pages or to your server.

## Example

View the [example](http://popomore.github.com/liquidluck-theme-reveal/ppt/2012/11/example.html).

Checkout gh-pages to view the [source](https://github.com/popomore/liquidluck-theme-reveal/blob/gh-pages/content/example.md).