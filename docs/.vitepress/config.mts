import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "lamr",
  description: "Code, exercises and resources to get you started with Python projects",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Start', link: '/readme/' },
      { text: 'Code', link: '/code' },
      { text: 'Manual', link: '/manual' }
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
        text: 'Beginner course',
        items: [
          { text: 'Project README', link: '/readme' },
        ]        
      },
      {
        text: 'Advanced topics',
        items: [
          { text: 'Project README', link: '/readme' },
        ]        
      },
      {
        text: 'Code examples',
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
