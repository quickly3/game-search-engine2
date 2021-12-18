17.hierarchies 层次结构
## [Hierarchies (d3-hierarchy)](https://github.com/d3/d3-hierarchy/tree/v3.0.1)

Layout algorithms for visualizing hierarchical data.用于可视化分层数据的布局算法。

-   [d3.hierarchy](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#hierarchy) - constructs a root node from hierarchical data.从分层数据构造一个根节点
-   [*node*.ancestors](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_ancestors) - generate an array of ancestors.
生成祖先数组
-   [*node*.descendants](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_descendants) - generate an array of descendants.生成后代数组
-   [*node*.leaves](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_leaves) - generate an array of leaves.生成叶子数组
-   [*node*.find](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_find) - find a node in the hierarchy.在层次结构中找到一个节点
-   [*node*.path](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_path) - generate the shortest path to another node.生成到另一个节点的最短路径
-   [*node*.links](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_links) - generate an array of links.生成链接数组
-   [*node*.sum](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_sum) - evaluate and aggregate quantitative values.评估和汇总定量值
-   [*node*.count](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_count) - count the number of leaves.计算叶子的数量
-   [*node*.sort](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_sort) - sort all descendant siblings.排序所有后代兄弟姐妹
-   [*node*[Symbol.iterator]](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_iterator) - iterate on a hierarchy.迭代层次结构
-   [*node*.each](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_each) - breadth-first traversal.广度优先遍历
-   [*node*.eachAfter](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_eachAfter) - post-order traversal.后序遍历
-   [*node*.eachBefore](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_eachBefore) - pre-order traversal.前序遍历
-   [*node*.copy](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#node_copy) - copy a hierarchy.复制层次结构
-   [d3.stratify](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#stratify) - create a new stratify operator.创建一个新的分层运算符
-   [*stratify*](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#_stratify) - construct a root node from tabular data.从表格数据构建根节点
-   [*stratify*.id](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#stratify_id) - set the node id accessor.设置节点 ID 访问器
-   [*stratify*.parentId](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#stratify_parentId) - set the parent node id accessor.设置父节点 ID 访问器
-   [d3.cluster](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#cluster) - create a new cluster (dendrogram) layout.创建一个新的集群（树状图）布局
-   [*cluster*](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#_cluster) - layout the specified hierarchy in a dendrogram.在树状图中布置指定的层次结构
-   [*cluster*.size](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#cluster_size) - set the layout size.设置布局大小
-   [*cluster*.nodeSize](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#cluster_nodeSize) - set the node size.设置节点大小
-   [*cluster*.separation](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#cluster_separation) - set the separation between leaves.设置叶子之间的间隔
-   [d3.tree](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#tree) - create a new tidy tree layout.创建一个新的整洁的树布局
-   [*tree*](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#_tree) - layout the specified hierarchy in a tidy tree.在整齐的树中布局指定的层次结构
-   [*tree*.size](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#tree_size) - set the layout size.设置布局大小
-   [*tree*.nodeSize](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#tree_nodeSize) - set the node size.设置节点大小
-   [*tree*.separation](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#tree_separation) - set the separation between nodes.设置节点之间的间隔
-   [d3.treemap](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap) - create a new treemap layout.创建新的树状图布局
-   [*treemap*](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#_treemap) - layout the specified hierarchy as a treemap.将指定的层次结构布局为树状图
-   [*treemap*.tile](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_tile) - set the tiling method.设置平铺方法
-   [*treemap*.size](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_size) - set the layout size.设置布局大小
-   [*treemap*.round](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_round) - set whether the output coordinates are rounded.设置输出坐标是否四舍五入
-   [*treemap*.padding](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_padding) - set the padding.设置填充
-   [*treemap*.paddingInner](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_paddingInner) - set the padding between siblings.设置兄弟姐妹之间的填充
-   [*treemap*.paddingOuter](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_paddingOuter) - set the padding between parent and children.设置父子之间的填充
-   [*treemap*.paddingTop](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_paddingTop) - set the padding between the parent’s top edge and children.设置父级顶部边缘和子级之间的填充
-   [*treemap*.paddingRight](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_paddingRight) - set the padding between the parent’s right edge and children.设置父级右边缘和子级之间的内边距
-   [*treemap*.paddingBottom](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_paddingBottom) - set the padding between the parent’s bottom edge and children.设置父级底部边缘和子级之间的内边距
-   [*treemap*.paddingLeft](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemap_paddingLeft) - set the padding between the parent’s left edge and children.设置父级左边缘和子级之间的内边距
-   [d3.treemapBinary](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemapBinary) - tile using a balanced binary tree.使用平衡二叉树平铺
-   [d3.treemapDice](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemapDice) - tile into a horizontal row.平铺成水平行
-   [d3.treemapSlice](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemapSlice) - tile into a vertical column.平铺成垂直列
-   [d3.treemapSliceDice](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemapSliceDice) - alternate between slicing and dicing.在切片和切块之间交替
-   [d3.treemapSquarify](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemapSquarify) - tile using squarified rows per Bruls *et. al.*使用每个 Bruls 的平方行平铺
-   [d3.treemapResquarify](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#treemapResquarify) - like d3.treemapSquarify, but performs stable updates.像 d3.treemapSquarify，但执行稳定更新
-   [*squarify*.ratio](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#squarify_ratio) - set the desired rectangle aspect ratio.设置所需的矩形纵横比
-   [d3.partition](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#partition) - create a new partition (icicle or sunburst) layout.创建一个新的分区（冰柱或森伯斯特）布局
-   [*partition*](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#_partition) - layout the specified hierarchy as a partition diagram.将指定的层次结构布局为分区图
-   [*partition*.size](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#partition_size) - set the layout size.设置布局大小
-   [*partition*.round](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#partition_round) - set whether the output coordinates are rounded.设置输出坐标是否四舍五入
-   [*partition*.padding](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#partition_padding) - set the padding.设置填充
-   [d3.pack](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#pack) - create a new circle-packing layout.创建一个新的圆形包装布局
-   [*pack*](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#_pack) - layout the specified hierarchy using circle-packing.使用圆形包装布局指定的层次结构
-   [*pack*.radius](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#pack_radius) - set the radius accessor.设置半径访问器
-   [*pack*.size](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#pack_size) - set the layout size.设置布局大小
-   [*pack*.padding](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#pack_padding) - set the padding.设置填充
-   [d3.packSiblings](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#packSiblings) - pack the specified array of circles.打包指定的圆数组
-   [d3.packEnclose](https://github.com/d3/d3-hierarchy/blob/v3.0.1/README.md#packEnclose) - enclose the specified array of circles.包含指定的圆数组