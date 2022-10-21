import { styled as materialStyled } from "@mui/material";
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';

const StyledTabList = materialStyled(TabList)(({ theme }) => ({
    minHeight: '35px',
    '& button': {
        flex: '1 1 0%',
        backgroundColor: 'rgba(217, 217, 217, 0.9)',
        color: 'black',
        fontFamily: 'Josefin Sans !important',
        fontStyle: 'normal',
        fontWeight: 300,
        fontSize: '20px',
        lineHeight: '20px',
        textTransform: 'initial',
        margin: '0px 1px',
        maxHeight: '35px',
        height: '35px',
        minHeight: '35px'
    },
    '& button.Mui-selected': {
        backgroundColor: 'white !important',
        color: 'black',
        fontWeight: 700
    }
}));

const StyledTabPanel = materialStyled(TabPanel)(({ theme }) => ({
    padding: '0px',
    paddingTop: '5px'
}));

export { StyledTabList, StyledTabPanel };