import { styled as materialStyled } from "@mui/material";
import Box from '@mui/material/Box';

export const Card = materialStyled(Box)(({ theme }) => ({
    backgroundColor: 'rgba(217, 217, 217, 0.9)',
    borderRadius: '15px',
    height: '85px',
    margin: '10px 0px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    flexDirection: 'column',
    '& h1': {
        fontFamily: 'Allison',
        fontStyle: 'normal',
        fontWeight: 400,
        fontSize: '60px',
        lineHeight: '76px'
    }
}));
