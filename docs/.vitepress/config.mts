import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "lamr",
  description:
    "Code, exercises and resources to get you started with Python projects",
  base: "/lamr/",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "Home", link: "/" },
      { text: "Start", link: "/readme/" },
      // { text: "Code", link: "/code" },
      // { text: "Manual", link: "/manual" },
    ],

    sidebar: [
      // {
      //   text: 'Beginner course',
      //   items: [
      //     { text: 'Project README', link: '/readme' },
      //   ]
      // },
      // {
      //   text: 'Advanced topics',
      //   items: [
      //     { text: 'Project README', link: '/readme' },
      //   ]
      // },
      {
        text: "Using lamr package",
        items: [
          { text: "Quickstart", link: "/readme/" },
          { text: "How to install", link: "/readme/how-to-install" },
          { text: "Motivation", link: "/readme/motivation" },
          { text: "Code snippets", link: "/readme/code" },
          { text: "Programming manual", link: "/readme/manual" },
        ]  
        },  
        {
          text: 'Study topics',
          items: [
            { text: 'What is programming?', link: '/topics/programming.md' },
            { text: 'Turing machine', link: '/topics/turing.md' },
              ]
        },
        {
        text: 'Code projects',
        items: [
          { text: 'Calendar', link: '/code/cal.py' },
          { text: 'ASCII art logo', link: '/code/logo.py' },
              // { text: 'Markdown Examples', link: '/markdown-examples' },
              // { text: 'Runtime API Examples', link: '/api-examples' }
            ]
        }
    ],

    socialLinks: [
      { icon: "github", link: "https://github.com/epogrebnyak/lamr" },
    ],
  },
});
