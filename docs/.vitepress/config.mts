import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "lamr",
  description: "Code, exercises and resources to get you started with Python projects",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'README', link: '/readme' },
      { text: 'Manual', link: '/manual' },
      { text: 'Code', link: '/code' }
    ],

    sidebar: [
      {
        text: 'Examples',
        items: [
          { text: 'Markdown Examples', link: '/markdown-examples' },
          { text: 'Runtime API Examples', link: '/api-examples' }
        ]        
      },
      {
        text: 'More',
        items: [
          { text: 'Project README', link: '/readme' },
        ]        
      }

    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/epogrebnyak/lamr' }
    ]
  }
})
