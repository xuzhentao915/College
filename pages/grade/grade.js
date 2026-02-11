// pages/grade/grade.js

Page({
    data: {
        navHeight: 0,
        semesters: ['2023-2024 第一学期', '2022-2023 第二学期', '2022-2023 第一学期'],
        index: 0,
        gpa: '3.82',
        grades: [
            { id: 1, name: '高等数学', type: '必修', credit: 4.0, score: 92, point: 4.0 },
            { id: 2, name: '英语文学鉴赏', type: '选修', credit: 2.0, score: 88, point: 3.7 },
            { id: 3, name: '计算机组成原理', type: '必修', credit: 3.5, score: 95, point: 4.0 },
            { id: 4, name: '物理实验', type: '实验', credit: 1.5, score: 85, point: 3.3 },
            { id: 5, name: '中国近代史纲要', type: '通识', credit: 2.0, score: 78, point: 2.7 }
        ]
    },

    onLoad() {
        const app = getApp();
        this.setData({ navHeight: app.globalData.navHeight });
    },

    bindPickerChange(e) {
        this.setData({ index: e.detail.value });
        // TODO: 实际应用中，此处应根据学期拉取新数据
    }
});
