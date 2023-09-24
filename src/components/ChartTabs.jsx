import { Tab, Tabs, TabList, TabPanel } from 'react-tabs'
import React, { useState } from 'react'
import './ChartTabsStyle.css';

function ChartTabs() {
  const [key, setKey] = useState('tab2')

  return (
    <div className="ChartTabs">
      <Tabs className="Tabs" activeKey={key} onSelect={(k) => setKey(k)}>
        <TabList>
          <Tab eventKey="tab1">Projection</Tab>
          <Tab eventKey="tab2">Distribution</Tab>
        </TabList>
        <TabPanel>
          <h3>Price Projection</h3>
          <img src="./public/static/images/linechart1.png" height="200" width="600" alt="linechart"></img>
        </TabPanel>
        <TabPanel>
          <h3>Crop Distribution!</h3>
          <img src="./public/static/images/piechart1.png" height="200" width="600" alt="piechart"></img>
        </TabPanel>
      </Tabs>
    </div>
  )
}

export default ChartTabs;