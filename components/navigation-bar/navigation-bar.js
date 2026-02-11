// components/navigation-bar/navigation-bar.js
Component({
  properties: {
    title: { type: String, value: 'College' },
    background: { type: String, value: 'transparent' },
    showBack: { type: Boolean, value: false },
    iconType: { type: String, value: 'home' } // home, schedule, grade, user
  },

  data: {
    navHeight: 0,
    menuTop: 0,
    menuHeight: 0
  },

  lifetimes: {
    attached() {
      const app = getApp();
      const { statusBarHeight, menuButtonInfo, navHeight } = app.globalData;
      
      this.setData({
        navHeight: navHeight,
        menuTop: menuButtonInfo.top,
        menuHeight: menuButtonInfo.height
      });
    }
  },

  methods: {
    handleLeftTap() {
      if (this.data.showBack) {
        wx.navigateBack();
      } else {
        this.triggerEvent('leftclick');
      }
    }
  }
});
