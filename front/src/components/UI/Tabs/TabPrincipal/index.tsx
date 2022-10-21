import React from "react";
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import { StyledTabList } from "./styles";
import { ConfiguracaoTabPrincipal, TabPrincipalEntradas } from "./entradas";
import { Link } from "react-router-dom";

export default function TabPrincipal({tabs}: TabPrincipalEntradas){
    const [tabAtual, definirTabAtual] = React.useState(tabs.findIndex(tab => window.location.href.includes(tab.rota)).toString());

    const aoSelecionarTab = (event: React.SyntheticEvent, tabSelecionada: string) => {
        definirTabAtual(tabSelecionada);
    };
  
    return (
        <Box sx={{ width: '880px' }}>
            <TabContext value={tabAtual}>
                <Box>
                    <StyledTabList onChange={aoSelecionarTab} centered>
                        {tabs.map((tab, index) => <Tab label={tab.rotulo} component={Link} to={tab.rota} value={index.toString()} key={index}/>)}
                    </StyledTabList>
                </Box>
            </TabContext>
        </Box>
    )
}