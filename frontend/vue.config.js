module.exports = {
  pages: {
    index: {
      entry: 'src/index/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'Index Page',
      chunks: ['chunk-vendors', 'chunk-common', 'index']
    },
    mobile: {
      entry: 'src/mobile/main.js',
      template: 'public/index.html',
      filename: 'mobile.html',
      title: 'Mobile Page',
      chunks: ['chunk-vendors', 'chunk-common', 'mobile']
    },
  },
  lintOnSave: false,
  outputDir: '../backend/dist',
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api*': {
        target: 'http://localhost:8000/',
      }
    }
  }
};
