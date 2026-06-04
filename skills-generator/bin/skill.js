#!/usr/bin/env node

import yargs from "yargs";
import { hideBin } from "yargs/helpers";

const argv = yargs(hideBin(process.argv))
  .option('dry-run', { alias: 'n', type: 'boolean', description: 'Simulate without making changes' })
  .parse();

console.log("CLI ready");
