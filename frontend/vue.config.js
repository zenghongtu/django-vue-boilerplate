module.exports = {
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
