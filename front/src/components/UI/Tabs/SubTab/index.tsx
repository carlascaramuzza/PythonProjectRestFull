import React from 'react';
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import { StyledTabList, StyledTabPanel } from './styles';
import { SubTabEntradas } from './entradas';

export default function SubTab({tabs}: SubTabEntradas){
    const [tabAtual, definirTabAtual] = React.useState('0');

    const aoSelecionarTab = (event: React.SyntheticEvent, tabSelecionada: string) => {
        definirTabAtual(tabSelecionada);
    };
  
    return (
        <Box sx={{ width: '880px' }}>
            <TabContext value={tabAtual}>
                <Box>
                    <StyledTabList onChange={aoSelecionarTab} centered>
                        {tabs.map((tab, index) => <Tab label={tab.rotulo} value={index.toString()} key={index}/>)}
                    </StyledTabList>
                </Box>
                {tabs.map((tab, index) => <StyledTabPanel value={index.toString()} key={index}>{tab.conteudo}</StyledTabPanel>)}
            </TabContext>
        </Box>
    )
}