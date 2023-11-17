// const { defineConfig } = require('@vue/cli-service')
// module.exports = defineConfig({
//   transpileDependencies: true,
  

// })

// module.exports = {
//   devServer: {
//     proxy: {
//       '/api': {
//         target: 'http://103.69.195.147:23031',
//         changeOrigin: true,
//         pathRewrite: { '^/api': '' },
//       },
//     },
//   },
// };
// module.exports = {
//   chainWebpack: config => {
//     // Modify the rule for images
//     config.module
//       .rule('images')
//       .use('url-loader')
//       .loader('url-loader')
//       .tap(options => {
//         options = options || {};
//         // Set esModule to false to avoid adding hash
//         options.esModule = false;
//         return options;
//       });
//   }
// };

// module.exports = defineConfig({
//   chainWebpack: config => {
//     // Xóa quy tắc cũ của url-loader
//     config.module.rules.delete('images');

//     // Thêm quy tắc mới sử dụng file-loader cho hình ảnh
//     config.module
//       .rule('images')
//       .test(/\.(png|jpe?g|gif|webp|svg|ico)(\?.*)?$/)
//       .use('file-loader')
//       .loader('file-loader')
//       .options({
//         name: '[name].[ext]',
//         outputPath: 'img',  // Thư mục đích cho các tệp ảnh
//       })
//       .end();
//   },
// })

const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: config => {
    config.module.rules.delete('images');

    //     // Thêm quy tắc mới sử dụng file-loader cho hình ảnh
        config.module
          .rule('images')
          .test(/\.(png|jpe?g|gif|webp|svg|ico)(\?.*)?$/)
          .use('file-loader')
          .loader('file-loader')
          .options({
            name: '[name].[ext]',
            //outputPath: '../assets/imgfood',
            outputPath: (url, resourcePath) => {
              // Determine the output path based on the resourcePath
              if (resourcePath.includes('imgfood')) {
                return `imgfood/${url}`;
              }
              return `img/${url}`;
            },
          })
          .end();
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'http://103.69.195.147:23031',
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    },
  },
});