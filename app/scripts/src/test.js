// Import the echarts core module, which provides the necessary interfaces for using echarts.
import * as echarts from 'echarts/core';
// Import bar charts, all with Chart suffix
import {
    BarChart
} from 'echarts/charts';
// import the prompt box, title, and rectangular coordinate system components, all suffixed with Component
import {
    TitleComponent,
    TooltipComponent,
    GridComponent
} from 'echarts/components';
// Import the Canvas renderer, note that introducing the CanvasRenderer or SVGRenderer is a required step
import {
    CanvasRenderer
} from 'echarts/renderers';

// Register the required components
echarts.use(
    [TitleComponent, TooltipComponent, GridComponent, BarChart, CanvasRenderer]
);

// The next step is the same as before, initialize the chart and set the configuration items
var myChart = echarts.init(document.getElementById('main'));
myChart.setOption({
    title: {
        text: 'ECharts Getting Started Example'
    },
    tooltip: {},
    xAxis: {
        data: ['shirt', 'cardigan', 'chiffon', 'pants', 'heels', 'socks']
    },
    yAxis: {},
    series: [{
        name: 'sales',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
    }]
});