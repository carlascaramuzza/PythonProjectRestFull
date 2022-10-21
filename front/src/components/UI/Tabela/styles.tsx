import styled from "@emotion/styled";
import { styled as materialStyled } from "@mui/material";
import { DataGrid as MuiDataGrid } from "@mui/x-data-grid";

const tamanhoTabela = 230;

const Container = styled.div`
  height: ${tamanhoTabela}px;
  width: 880px;
  background-color: rgba(217, 217, 217, 0.9);
`;

const DataGrid = materialStyled(MuiDataGrid)(({ theme }) => ({
    '& .MuiDataGrid-cell': {
        backgroundColor: 'white',
        marginLeft: '10px',
        marginRight: '10px',
        fontFamily: 'Josefin Sans',
        fontStyle: 'normal',
        fontWeight: 400,
        fontSize: '20px',
        lineHeight: '20px'
    },
    '& .MuiDataGrid-row:hover': {
        backgroundColor: 'inherit'
    },
    "& .MuiDataGrid-columnHeaders": { display: "none" },
    "& .MuiDataGrid-virtualScroller": { marginTop: "0!important", height: `${tamanhoTabela}px!important` },
}));

export {DataGrid, Container};