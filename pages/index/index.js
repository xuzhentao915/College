// pages/index/index.js

Page({
    data: {
        navHeight: 0,
        currentDate: '',
        greeting: '',
        todayCourses: [
            { id: 1, time: '08:00', name: '高等数学', room: 'A-101' },
            { id: 2, time: '10:00', name: '英语文学鉴赏', room: 'B-305' },
            { id: 3, time: '14:00', name: '计算机组成原理', room: 'C-202' }
        ],
        notices: [
            { id: 1, title: '2023-2024学年考试安排通知', date: '10/24' },
            { id: 2, title: '国庆节放假安排', date: '10/01' },
            { id: 3, title: '图书馆闭馆维修通知', date: '09/15' }
        ]
    },

    onLoad() {
        const app = getApp();
        this.setData({
            navHeight: app.globalData.navHeight
        });
        this.updateDateTime();
    },

    onShow() {
        // 每次页面展示时更新时间问候语
        this.updateDateTime();
    },

    /**
     * 根据当前时间更新日期和问候语
     */
    updateDateTime() {
        const now = new Date();
        const hour = now.getHours();

        let greeting = '早上好';
        if (hour >= 12 && hour < 14) greeting = '中午好';
        else if (hour >= 14 && hour < 18) greeting = '下午好';
        else if (hour >= 18) greeting = '晚上好';

        const options = { month: 'long', day: 'numeric', weekday: 'long' };
        this.setData({
            greeting,
            currentDate: now.toLocaleDateString('zh-CN', options)
        });
    },

    navigateTo(e) {
        const url = e.currentTarget.dataset.url;
        if (!url) return;

        wx.switchTab({
            url,
            fail: () => {
                wx.navigateTo({ url });
            }
        });
    }
});
