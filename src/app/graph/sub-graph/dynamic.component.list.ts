import { SourceStatistics } from './source-statistics/source-statistics.component';
import { SourceStatisticsLastDay } from './source-statistics-lastday/source-statistics-lastday.component';
import { CateStatistics } from './cate-statistics/cate-statistics.component';


const components = [
  {
    name: 'SourceStatistics',
    title: '全部数据分布',
    component: SourceStatistics,
  },
  {
    name: 'SourceStatisticsLastDay',
    title: '昨日全部数据分布',
    component: SourceStatisticsLastDay,
  },
  {
    name: 'CateStatistics',
    title: '文章分类分布',
    component: CateStatistics,
  },
];

const getComponentByName = (name) => {
  return components.find((c) => {
    return c.name === name;
  });
};

export default {
  components,
  getComponentByName,
};
