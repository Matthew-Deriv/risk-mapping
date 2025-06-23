import { useState, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import remarkGfm from "remark-gfm";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";
import {
  CssBaseline,
  Drawer,
  List,
  ListItemButton,
  Box,
  Paper,
  Typography,
} from "@mui/material";

/**
 * Markdown viewer with KaTeX math + GitHub‑style tables (GFM).
 * Expands content to full width so long tables/images don't require horizontal scroll.
 * -----------------------------------------------------------------
 * One‑time deps if not installed yet:
 *   npm i @mui/material @emotion/react @emotion/styled react-markdown remark-math remark-gfm rehype-katex katex
 */

const drawerWidth = 240;

const reports = [
  { id: "multistep", label: "Multistep Indices", file: "/multistep_reports.md" },
  // { id: "skewstep", label: "Skew Step", file: "/skewstep_report.md" },
];

export default function App() {
  const [current, setCurrent] = useState(reports[0]);
  const [mdSrc, setMdSrc] = useState("Loading…");

  useEffect(() => {
    fetch(current.file)
      .then((r) => r.text())
      .then(setMdSrc)
      .catch(() => setMdSrc("⚠️ Unable to load report."));
  }, [current]);

  return (
    <>
      <CssBaseline />
      <Drawer
        variant="permanent"
        sx={{ width: drawerWidth, [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: "border-box" } }}
      >
        <Box sx={{ p: 2 }}>
          <Typography variant="h6">Reports</Typography>
        </Box>
        <List>
          {reports.map((r) => (
            <ListItemButton key={r.id} selected={r.id === current.id} onClick={() => setCurrent(r)}>
              {r.label}
            </ListItemButton>
          ))}
        </List>
      </Drawer>

      <Box component="main" sx={{ ml: `${drawerWidth}px`, p: 3 }}>
        {/*
          * Remove the fixed maxWidth so the Paper can stretch to the available
          * viewport. "overflowX: auto" remains as a safety net for *very* wide
          * assets but in normal cases the table/image will now fit without a
          * horizontal scrollbar.
          */}
        <Paper sx={{ p: 3, width: "100%", overflowX: "auto" }}>
          <ReactMarkdown
            remarkPlugins={[remarkMath, remarkGfm]}
            rehypePlugins={[rehypeKatex]}
          >
            {mdSrc}
          </ReactMarkdown>
        </Paper>
      </Box>
    </>
  );
}
