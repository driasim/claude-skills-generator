#!/usr/bin/env node

import yargs from "yargs";
import { hideBin } from "yargs/helpers";

const argv = yargs(hideBin(process.argv))
  .option('config', { alias: 'c', type: 'string', description: 'Path to config file' })
  .parse();

console.log("CLI ready");
