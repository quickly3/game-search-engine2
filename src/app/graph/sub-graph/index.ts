import { DynamicSubGraph } from './dynamic-sub-graph.component';
import { SubGraph } from './subGraph.directive';
import { SourceStatistics } from './source-statistics/source-statistics.component';
import { SourceStatisticsLastDay } from './source-statistics-lastday/source-statistics-lastday.component';
import { CateStatistics } from './cate-statistics/cate-statistics.component';
import { DataCalendar } from './data-calendar/data-calendar.component';
import { JuejinWordCloud } from './juejin-wordcloud/juejin-wordcloud.component';




const subComponents = [
  SourceStatistics,
  SourceStatisticsLastDay,
  CateStatistics,
  DataCalendar,
  JuejinWordCloud
];

const allComponents = [
  SubGraph,
  DynamicSubGraph,
  ...subComponents
];

export default {
  allComponents,
  subComponents
};
