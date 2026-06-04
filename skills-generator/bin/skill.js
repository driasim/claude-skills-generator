#!/usr/bin/env node

import yargs from "yargs";
import { hideBin } from "yargs/helpers";

const argv = yargs(hideBin(process.argv))
  .option('verbose', { alias: 'v', type: 'boolean', description: 'Enable verbose output' })
  .parse();

console.log("CLI ready");
