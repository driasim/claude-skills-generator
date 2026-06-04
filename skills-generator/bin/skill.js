#!/usr/bin/env node

import yargs from "yargs";
import { hideBin } from "yargs/helpers";

const argv = yargs(hideBin(process.argv))
  .option('format', { type: 'string', choices: ['json', 'markdown'], description: 'Output format (json/markdown)' })
  .parse();

console.log("CLI ready");
