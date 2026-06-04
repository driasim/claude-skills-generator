#!/usr/bin/env node

import yargs from "yargs";
import { hideBin } from "yargs/helpers";

const argv = yargs(hideBin(process.argv))
  .option('force', { type: 'boolean', description: 'Force operations without confirmation' })
  .parse();

console.log("CLI ready");
