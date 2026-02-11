// pages/user/user.js

Page({
    handleTap(e) {
        const action = e.currentTarget.dataset.action;

        switch (action) {
            case 'grades':
                wx.switchTab({ url: '/pages/grade/grade' });
                break;
            case 'schedule':
                wx.switchTab({ url: '/pages/schedule/schedule' });
                break;
            default:
                wx.showToast({ title: '功能开发中', icon: 'none' });
        }
    }
});
