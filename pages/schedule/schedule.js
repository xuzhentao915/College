// pages/schedule/schedule.js

Page({
    data: {
        navHeight: 0,
        weekDays: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
        selectedDay: 0,
        courses: {
            0: [
                { id: 1, startTime: '08:00', endTime: '09:35', name: '高等数学', room: 'A-101', teacher: '张教授', color: '#409EFF' },
                { id: 2, startTime: '10:00', endTime: '11:35', name: '英语文学鉴赏', room: 'B-305', teacher: '李老师', color: '#67C23A' }
            ],
            1: [
                { id: 3, startTime: '14:00', endTime: '15:35', name: '计算机组成原理', room: 'C-202', teacher: '王博士', color: '#E6A23C' }
            ],
            2: [
                { id: 4, startTime: '08:00', endTime: '09:35', name: '大学物理', room: 'D-401', teacher: '陈教授', color: '#F56C6C' },
                { id: 5, startTime: '10:00', endTime: '11:35', name: '近代史纲要', room: 'E-102', teacher: '吴老师', color: '#909399' }
            ],
            3: [
                { id: 6, startTime: '09:00', endTime: '11:00', name: '艺术选修', room: '艺术楼', teacher: '周老师', color: '#409EFF' }
            ],
            4: [
                { id: 7, startTime: '08:00', endTime: '09:35', name: '高等数学', room: 'A-101', teacher: '张教授', color: '#409EFF' },
                { id: 8, startTime: '13:00', endTime: '14:35', name: '体育', room: '体育馆', teacher: '刘教练', color: '#67C23A' }
            ],
            5: [],
            6: []
        }
    },

    onLoad() {
        const app = getApp();
        this.setData({ navHeight: app.globalData.navHeight });
        this._autoSelectToday();
    },

    /**
     * 自动选中今天对应的星期
     * JS getDay(): 0=周日, 1=周一 ... 6=周六
     * 我们需要: 0=周一 ... 6=周日
     */
    _autoSelectToday() {
        const jsDay = new Date().getDay();
        const adjustedDay = jsDay === 0 ? 6 : jsDay - 1;
        this.setData({ selectedDay: adjustedDay });
    },

    selectDay(e) {
        this.setData({
            selectedDay: e.currentTarget.dataset.index
        });
    }
});
