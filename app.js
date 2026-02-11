// app.js

App({
  globalData: {
    systemInfo: null,
    navHeight: 0, // 导航栏高度
    statusBarHeight: 0, // 状态栏高度
    menuButtonInfo: null, // 胶囊信息
    safeAreaBottom: 0, // 底部安全区
  },

  onLaunch() {
    // 1. 获取系统信息
    const info = wx.getSystemInfoSync();
    this.globalData.systemInfo = info;
    this.globalData.statusBarHeight = info.statusBarHeight;
    
    // 2. 获取胶囊信息 (仅小程序)
    const menuButton = wx.getMenuButtonBoundingClientRect();
    this.globalData.menuButtonInfo = menuButton;

    // 3. 计算自定义导航栏高度
    // 公式：导航栏高度 = 状态栏高度 + (胶囊距离顶部距离 - 状态栏高度) * 2 + 胶囊高度
    this.globalData.navHeight = info.statusBarHeight + (menuButton.top - info.statusBarHeight) * 2 + menuButton.height;

    // 4. 计算底部安全距离 (iOS 底部横条)
    this.globalData.safeAreaBottom = info.screenHeight - info.safeArea.bottom;

    console.log('📱 适配信息:', {
      OS: info.platform,
      Nav: this.globalData.navHeight,
      Bottom: this.globalData.safeAreaBottom
    });
  }
});
