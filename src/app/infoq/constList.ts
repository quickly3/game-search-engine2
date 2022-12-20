const tagsI18n = [
    { text: 'All', i18n: '全部' },
    { text: 'Python', i18n: 'Python' },
    { text: 'PHP', i18n: 'PHP' },
    { text: 'Javascript', i18n: 'Javascript' },
    { text: 'Css', i18n: 'Css' },
    { text: 'Typescript', i18n: 'Typescript' },
    { text: 'Node', i18n: 'Node' },
    { text: 'Game', i18n: '游戏' },
    { text: 'Security', i18n: '安全' },
    { text: 'Linux', i18n: 'Linux' },
    { text: 'Postgresql', i18n: 'Postgres' },
    // {text: "blockchain", i18n: "区块链"},
    { text: 'blockchain', i18n: '区块链' },
    { text: 'dp', i18n: '设计模式' },
    { text: 'design', i18n: '设计' },
    { text: 'opensource', i18n: '开源' },
    { text: 'nosql', i18n: 'Nosql' },
    { text: 'game', i18n: '游戏' },
    { text: 'web', i18n: '网页开发' },
    { text: 'algorithm', i18n: '算法' },
    { text: 'translate', i18n: '翻译' },
];

const sortItems = [
    { value: 'multi', label: '综合' },
    { value: 'date', label: '日期' },
    { value: 'score', label: '搜索相关度' },
    { value: 'viewed', label: '阅读' },
    { value: 'like', label: '点赞' },
    { value: 'comments', label: '评论' },
    { value: 'collected', label: '收藏' },
];

const authorSortItems = [
    { value: 'post_article_count', label: '文章数' },
    { value: 'power', label: '掘力值' },
    { value: 'level', label: 'Level' }

]

const sourceList = [
    { title: 'all', source_class: 'icon-all', text: '全部' },
    { title: 'github', source_class: 'icon-github', text: 'GitHub' },
    { title: 'jianshu', source_class: 'icon-jianshu', text: '简书' },
    { title: 'infoq', source_class: 'icon-infoq', text: '极客帮' },
    { title: 'bilibili', source_class: 'icon-bilibili', text: '极客帮' },
    { title: 'juejin', source_class: 'icon-juejin', text: '掘金' },
    { title: 'cnblogs', source_class: 'icon-cnblogs', text: '博客园' },
    { title: 'csdn', source_class: 'icon-csdn', text: 'CSDN' },
    { title: 'oschina', source_class: 'icon-oschina', text: '开源中国' },
    { title: 'sf', source_class: 'icon-sf', text: '思否' },
    { title: 'escn', source_class: 'icon-escn', text: 'Es中文社区' },
    { title: 'elastic', source_class: 'icon-elastic', text: 'Es官方' },
    { title: 'itpub', source_class: 'icon-itpub', text: 'itpub' },
    {
        title: 'data_whale',
        source_class: 'icon-datawhale',
        text: '和鲸数据',
    },
    {
        title: 'ali_dev',
        source_class: 'icon-alidev',
        text: '阿里开发者社区',
    },
    {
        title: '36kr',
        source_class: 'icon-36kr',
        text: '36氪',
    },


];


const displayModelItems = [
    { value: 'summary', label: '简介模式' },
    { value: 'title', label: '标题模式' },
];

const constList = {
    tagsI18n,
    sortItems,
    sourceList,
    displayModelItems,
    authorSortItems
};

export default constList;
