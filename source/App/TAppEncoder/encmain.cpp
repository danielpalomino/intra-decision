/* The copyright in this software is being made available under the BSD
 * License, included below. This software may be subject to other third party
 * and contributor rights, including patent rights, and no such rights are
 * granted under this license.  
 *
 * Copyright (c) 2010-2012, ITU/ISO/IEC
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *  * Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 *  * Neither the name of the ITU/ISO/IEC nor the names of its contributors may
 *    be used to endorse or promote products derived from this software without
 *    specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 * THE POSSIBILITY OF SUCH DAMAGE.
 */

/** \file     encmain.cpp
    \brief    Encoder application main
*/

#include <time.h>
#include <sys/time.h>
#include "TAppEncTop.h"

//! \ingroup TAppEncoder
//! \{

// ====================================================================================================================
// Main function
// ====================================================================================================================

//DANIEL BEGIN
FILE *modes;
FILE *input_modes;
FILE *results;
Int level8, level16, level32, level64;
Bool mySearch;
//DANIEL END
int main(int argc, char* argv[])
{
  TAppEncTop  cTAppEncTop;

  // print information
  fprintf( stdout, "\n" );
  fprintf( stdout, "HM software: Encoder Version [%s]", NV_VERSION );
  fprintf( stdout, NVM_ONOS );
  fprintf( stdout, NVM_COMPILEDBY );
  fprintf( stdout, NVM_BITS );
  fprintf( stdout, "\n" );

  // create application encoder class
  cTAppEncTop.create();

  // parse configuration
  if(!cTAppEncTop.parseCfg( argc, argv ))
  {
    cTAppEncTop.destroy();
    return 1;
  }

  //DANIEL BEGIN
  int file;
  modes = fopen("modes", "w");
  results = fopen("results","w");
  if (mySearch)
  {
    input_modes = fopen("input_modes","r");
    file = fscanf(input_modes,"%d",&level8);
    file = fscanf(input_modes,"%d",&level16);
    file = fscanf(input_modes,"%d",&level32);
    file = fscanf(input_modes,"%d",&level64);
  }
  //DANIEL END

  // starting time
  double dResult;
  long lBefore = clock();
  //DANIEL BEGIN
  double diff_time;
  static struct timeval timer_start, timer_end;
  gettimeofday(&timer_start, NULL);
  //DANIEL END

  // call encoding function
  cTAppEncTop.encode();

  // ending time
  dResult = (double)(clock()-lBefore) / CLOCKS_PER_SEC;
  printf("\n Total Time: %12.3f sec.\n", dResult);
  //DANIEL BEGIN
  gettimeofday(&timer_end,NULL);
  diff_time = timer_end.tv_sec - timer_start.tv_sec + (timer_end.tv_usec - timer_start.tv_usec) / 1000000.0;

  // destroy application encoder class
  cTAppEncTop.destroy();

  //DANIEL BEGIN
  fprintf(results,"%.3f\n",diff_time);
  fclose(modes);
  fclose(results);
  if(mySearch)
    fclose(input_modes);
  //DANIEL END

  return 0;
}

//! \}
