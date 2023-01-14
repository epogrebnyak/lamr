export default {   
    title: 'Basic Site',   
    description: 'Not just playing around.',
    themeConfig: {
        nav: [
          { text: 'Slides', link: '/slides' },
        ],
        sidebar: [{
            // This sidebar gets displayed when user is
            // under `guide` directory.
                text: 'Guide',
                items: [
                  // This shows `/guide/index.md` page.
                  { text: 'Index', link: '/page' }, // /guide/index.md
                  { text: 'Index', link: '/slides' }, // /guide/index.md
                ]
              }
        ]
}
}