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
    let menuButton = { top: 0, height: 32, left: 0 };
    try {
      menuButton = wx.getMenuButtonBoundingClientRect();
    } catch (e) {
      console.error('获取胶囊信息失败', e);
    }
    this.globalData.menuButtonInfo = menuButton;

    // 3. 计算自定义导航栏高度 (容错处理)
    const statusBarHeight = info.statusBarHeight || 20;
    const top = menuButton.top || (statusBarHeight + 4);
    const height = menuButton.height || 32;
    this.globalData.navHeight = statusBarHeight + (top - statusBarHeight) * 2 + height;

    // 4. 计算底部安全距离 (iOS 底部横条)
    this.globalData.safeAreaBottom = info.screenHeight - info.safeArea.bottom;

    console.log('📱 适配信息:', {
      OS: info.platform,
      Nav: this.globalData.navHeight,
      Bottom: this.globalData.safeAreaBottom
    });
  }
});
