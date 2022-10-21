import { styled as materialStyled } from "@mui/material";
import TabPanel from '@mui/lab/TabPanel';
import TabList from '@mui/lab/TabList';

export const StyledTabList = materialStyled(TabList)(({ theme }) => ({
    borderRadius: '15px',
    minHeight: '33px',
    '& button, a': {
        flex: '1 1 0%',
        backgroundColor: 'rgba(222, 195, 82, 0.9)',
        color: 'black',
        fontFamily: 'Josefin Sans !important',
        fontStyle: 'normal',
        fontWeight: 700,
        fontSize: '20px',
        lineHeight: '20px',
        textTransform: 'initial',
        maxHeight: '33px',
        height: '33px',
        minHeight: '33px'
    },
    '& button.Mui-selected, a.Mui-selected': {
        border: '2px solid #000000',
        backgroundColor: '#DBBF5D',
        color: 'black'
    }
}));

export const StyledTabPanel = materialStyled(TabPanel)(({ theme }) => ({
    padding: '0px',
    paddingTop: '5px'
}));