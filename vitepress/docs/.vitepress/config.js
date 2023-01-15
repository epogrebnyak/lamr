export default {   
    title: 'Jump Into Programming with Python',   
    description: 'Not just playing around.',
    themeConfig: {
        nav: [
          { text: 'Slides', link: '/slides' },
        ],
        sidebar: [
          {text: 'Getting started', 
           items: [
             {text: 'Where to run code', link: '/environments'}
           ]},
          {
          text: 'Minimal Python',
                items: [
                  { text: 'Values and operators', link: '/values_and_operators' }, 
                  { text: 'Variables', link: '/variables' }, 
                  { text: 'Sequences', link: '/sequences' }, 
                  { text: 'Control flow', link: '/flow' }, 
                  { text: 'Functions', link: '/functions' },
                  { text: 'Modules and packages', link: '/import' }, 
                  { text: 'Input and output', link: '/io' }, 
                ]
              }, 
              {
                text: 'Next to learn ',
                items: [
            { text: 'Dictionaries', link: '\dictionaries' },
            { text: 'Comprehensions', link: '\comprehensions' },
            { text: '`while` loops', link: '\while' },
            { text: 'Exceptions', link: '\exceptions' },
            { text: 'OOP and classes', link: '\OOP' },
            ]
              },

        ]
}
}

