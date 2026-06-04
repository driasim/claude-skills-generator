#!/usr/bin/env node

import yargs from "yargs";
import { hideBin } from "yargs/helpers";

const argv = yargs(hideBin(process.argv))
  .option('yes', { alias: 'y', type: 'boolean', description: 'Auto-confirm all prompts' })
  .parse();

console.log("CLI ready");
