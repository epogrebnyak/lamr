const path = require( "path" );
const fs = require('fs');

function parseSidebar () {
    fp = path.resolve(__dirname, 'sidebar.json')
    data = fs.readFileSync(fp, 'utf8');
    return JSON.parse(data) || {} 
}

export default {   
    title: 'Jump Into Programming with Python',   
    description: 'Not just playing around.',
    themeConfig: {
        nav: [
          { text: 'Slides', link: '/slides' },
        ],
        // TODO: sidebar value should be imported from sidebar.json 
        // This does not work as file is not found:
        //    sidebar: parseSidebar ()
        sidebar: parseSidebar (),
        sidebar_: [
          {
              "text": "Getting started",
              "items": [
                  {
                      "text": "Where to run code",
                      "link": "/environments"
                  }
              ]
          },
          {
              "text": "Minimal Python",
              "items": [
                  {
                      "text": "Values and operators",
                      "link": "/values_and_operators"
                  },
                  {
                      "text": "Variables",
                      "link": "/variables"
                  },
                  {
                      "text": "Sequences",
                      "link": "/sequences"
                  },
                  {
                      "text": "Control flow",
                      "link": "/flow"
                  },
                  {
                      "text": "Functions and methods",
                      "link": "/functions"
                  },
                  {
                      "text": "Modules and packages",
                      "link": "/import"
                  },
                  {
                      "text": "Input and output",
                      "link": "/io"
                  }
              ]
          },
          {
              "text": "Learn next",
              "items": [
                  {
                      "text": "Dictionaries",
                      "link": "/dictionaries"
                  },
                  {
                      "text": "Comprehensions",
                      "link": "/comprehensions"
                  },
                  {
                      "text": "`while` loops",
                      "link": "/while"
                  },
                  {
                      "text": "Exceptions",
                      "link": "/exceptions"
                  },
                  {
                      "text": "OOP and classes",
                      "link": "/OOP"
                  }
              ]
          }
      ]
}
}

