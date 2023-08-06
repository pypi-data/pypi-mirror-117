#include "nlp_common/WordAlignmentMatrix.h"

WordAlignmentMatrix::WordAlignmentMatrix()
{
  I = 0;
  J = 0;
}

WordAlignmentMatrix::WordAlignmentMatrix(unsigned int I_dims, unsigned int J_dims)
{
  I = 0;
  J = 0;
  init(I_dims, J_dims);
}

WordAlignmentMatrix::WordAlignmentMatrix(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;

  I = 0;
  J = 0;
  init(waMatrix.I, waMatrix.J);

  for (i = 0; i < I; ++i)
    for (j = 0; j < J; ++j)
      matrix[i][j] = waMatrix.matrix[i][j];
}

unsigned int WordAlignmentMatrix::get_I() const
{
  return I;
}

unsigned int WordAlignmentMatrix::get_J() const
{
  return J;
}

unsigned int WordAlignmentMatrix::getValue(unsigned int i, unsigned int j) const
{
  return matrix[i][j];
}

void WordAlignmentMatrix::init(unsigned int I_dims, unsigned int J_dims)
{
  unsigned int i;

  if (I != I_dims || J != J_dims)
  {
    clear();
    I = I_dims;
    J = J_dims;

    matrix = (unsigned int**)calloc(I, sizeof(unsigned int*));
    for (i = 0; i < I; ++i)
      matrix[i] = (unsigned int*)calloc(J, sizeof(unsigned int));

    reset();
  }
  else
    reset();
}

void WordAlignmentMatrix::putAligVec(std::vector<PositionIndex> aligVec)
{
  unsigned int j;

  if (aligVec.size() == J)
  {
    for (j = 0; j < aligVec.size(); ++j)
    {
      if (aligVec[j] > 0)
        matrix[aligVec[j] - 1][j] = 1;
    }
  }
}

bool WordAlignmentMatrix::getAligVec(std::vector<PositionIndex>& aligVec) const
{
  aligVec.clear();
  for (unsigned int j = 0; j < J; ++j)
  {
    aligVec.push_back(0);
    for (unsigned int i = 0; i < I; ++i)
    {
      if (matrix[i][j] != 0)
      {
        if (aligVec[j] == 0)
          aligVec[j] = i + 1;
        else
        {
          aligVec.clear();
          return false;
        }
      }
    }
  }
  return true;
}

void WordAlignmentMatrix::reset(void)
{
  unsigned int i, j;

  for (i = 0; i < I; ++i)
    for (j = 0; j < J; ++j)
      matrix[i][j] = 0;
}

void WordAlignmentMatrix::set(void)
{
  unsigned int i, j;

  for (i = 0; i < I; ++i)
    for (j = 0; j < J; ++j)
      matrix[i][j] = 1;
}

void WordAlignmentMatrix::set(unsigned int i, unsigned int j)
{
  if (i < I && j < J)
    matrix[i][j] = 1;
}

void WordAlignmentMatrix::setValue(unsigned int i, unsigned int j, unsigned int val)
{
  if (i < I && j < J)
    matrix[i][j] = val;
}

void WordAlignmentMatrix::transpose(void)
{
  WordAlignmentMatrix wam;
  unsigned int i, j;

  wam.init(J, I);

  for (i = 0; i < I; ++i)
    for (j = 0; j < J; ++j)
    {
      wam.matrix[j][i] = matrix[i][j];
    }
  *this = wam;
}

WordAlignmentMatrix& WordAlignmentMatrix::operator=(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;

  init(waMatrix.I, waMatrix.J);
  for (i = 0; i < I; ++i)
    for (j = 0; j < J; ++j)
      matrix[i][j] = waMatrix.matrix[i][j];

  return *this;
}

bool WordAlignmentMatrix::operator==(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;

  if (waMatrix.I != I || waMatrix.J != J)
    return 0;
  for (i = 0; i < I; ++i)
    for (j = 0; j < J; ++j)
    {
      if (waMatrix.matrix[i][j] != matrix[i][j])
        return 0;
    }

  return 1;
}

WordAlignmentMatrix& WordAlignmentMatrix::flip(void)
{
  unsigned int i, j;

  for (i = 0; i < I; ++i)
    for (j = 0; j < J; ++j)
    {
      if (matrix[i][j] == 0)
        matrix[i][j] = 1;
      else
        matrix[i][j] = 0;
    }
  return *this;
}

WordAlignmentMatrix& WordAlignmentMatrix::operator&=(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;

  if (I == waMatrix.I && J == waMatrix.J)
  {
    for (i = 0; i < I; ++i)
      for (j = 0; j < J; ++j)
      {
        if (!(matrix[i][j] != 0 && waMatrix.matrix[i][j] != 0))
          matrix[i][j] = 0;
      }
  }
  return *this;
}

WordAlignmentMatrix& WordAlignmentMatrix::operator|=(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;

  if (I == waMatrix.I && J == waMatrix.J)
  {
    for (i = 0; i < I; ++i)
      for (j = 0; j < J; ++j)
        if (matrix[i][j] != 0 || waMatrix.matrix[i][j] != 0)
          matrix[i][j] = 1;
  }
  return *this;
}

WordAlignmentMatrix& WordAlignmentMatrix::operator^=(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;

  if (I == waMatrix.I && J == waMatrix.J)
  {
    for (i = 0; i < I; ++i)
      for (j = 0; j < J; ++j)
      {
        if ((matrix[i][j] != 0 && waMatrix.matrix[i][j] == 0) || (matrix[i][j] == 0 && waMatrix.matrix[i][j] != 0))
          matrix[i][j] = 1;
        else
          matrix[i][j] = 0;
      }
  }
  return *this;
}

WordAlignmentMatrix& WordAlignmentMatrix::operator+=(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;

  if (I == waMatrix.I && J == waMatrix.J)
  {
    for (i = 0; i < I; ++i)
      for (j = 0; j < J; ++j)
        matrix[i][j] = matrix[i][j] + waMatrix.matrix[i][j];
  }
  return *this;
}

WordAlignmentMatrix& WordAlignmentMatrix::operator-=(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;

  if (I == waMatrix.I && J == waMatrix.J)
  {
    for (i = 0; i < I; ++i)
      for (j = 0; j < J; ++j)
        if (matrix[i][j] != 0 && waMatrix.matrix[i][j] == 0)
          matrix[i][j] = 1;
  }
  return *this;
}

WordAlignmentMatrix& WordAlignmentMatrix::symmetr1(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;
  WordAlignmentMatrix aux, prev;

  if (I == waMatrix.I && J == waMatrix.J)
  {
    aux = *this;
    *this &= waMatrix;
    prev.reset();

    while (!(*this == prev))
    {
      prev = *this;
      for (i = 0; i < I; ++i)
        for (j = 0; j < J; ++j)
        {
          if ((waMatrix.matrix[i][j] != 0 || aux.matrix[i][j] != 0) && this->matrix[i][j] == 0)
          {
            if (!jAligned(j) && !iAligned(i))
              this->matrix[i][j] = 1;
            else
            {
              if (this->ijInNeighbourhood(i, j))
                this->matrix[i][j] = 1;
            }
          }
        }
    }
  }
  return *this;
}

WordAlignmentMatrix& WordAlignmentMatrix::symmetr2(const WordAlignmentMatrix& waMatrix)
{
  unsigned int i, j;
  WordAlignmentMatrix aux;
  WordAlignmentMatrix prev;

  if (I == waMatrix.I && J == waMatrix.J)
  {
    aux = *this;
    *this &= waMatrix;
    prev.reset();

    while (!(*this == prev))
    {
      prev = *this;
      for (i = 0; i < I; ++i)
        for (j = 0; j < J; ++j)
        {
          if ((waMatrix.matrix[i][j] != 0 || aux.matrix[i][j] != 0) && this->matrix[i][j] == 0)
          {
            if (!jAligned(j) && !iAligned(i))
              this->matrix[i][j] = 1;
            else
            {
              if (this->ijInNeighbourhood(i, j))
                if (!(this->ijHasHorizNeighbours(i, j) && this->ijHasVertNeighbours(i, j)))
                  this->matrix[i][j] = 1;
            }
          }
        }
    }
  }
  return *this;
}

WordAlignmentMatrix& WordAlignmentMatrix::growDiagFinal(const WordAlignmentMatrix& waMatrix)
{
  // Check that the matrices can be operated
  if (I != waMatrix.I || J != waMatrix.J)
  {
    return *this;
  }
  else
  {
    // Matrices can be operated

    // Obtain copy of source matrix
    WordAlignmentMatrix sourceMatAux = *this;

    // Obtain intersection between source and target
    *this &= waMatrix;

    // Obtain union between source and target
    WordAlignmentMatrix joinMat = sourceMatAux;
    joinMat |= waMatrix;

    // Grow-diag
    bool end = false;
    WordAlignmentMatrix prevMat = *this;

    // Iterate until no new points added
    while (!end)
    {
      for (unsigned int i = 0; i < I; ++i)
      {
        for (unsigned int j = 0; j < J; ++j)
        {
          // Check if (i,j) is aligned
          if (getValue(i, j))
          {
            // Explore neighbourhood
            std::vector<std::pair<unsigned int, unsigned int>> neighboursVec = obtainAdjacentCells(i, j);
            for (unsigned int k = 0; k < neighboursVec.size(); ++k)
            {
              unsigned int ip = neighboursVec[k].first;
              unsigned int jp = neighboursVec[k].second;
              if ((!iAligned(ip) || !jAligned(jp)) && joinMat.getValue(ip, jp))
              {
                set(ip, jp);
              }
            }
          }
        }
      }
      if (prevMat == *this)
        end = true;
      else
        prevMat = *this;
    }

    // Final source
    for (unsigned int i = 0; i < I; ++i)
    {
      for (unsigned int j = 0; j < J; ++j)
      {
        if ((!iAligned(i) || !jAligned(j)) && sourceMatAux.getValue(i, j))
        {
          set(i, j);
        }
      }
    }

    // Final target
    for (unsigned int i = 0; i < I; ++i)
    {
      for (unsigned int j = 0; j < J; ++j)
      {
        if ((!iAligned(i) || !jAligned(j)) && waMatrix.getValue(i, j))
        {
          set(i, j);
        }
      }
    }

    // Return result
    return *this;
  }
}

std::vector<std::pair<unsigned int, unsigned int>> WordAlignmentMatrix::obtainAdjacentCells(unsigned int i,
                                                                                            unsigned int j)
{
  // Initialize variables
  std::vector<std::pair<unsigned int, unsigned int>> puintVec;

  // Add neighbour points
  for (int delta_i = -1; delta_i <= 1; ++delta_i)
  {
    for (int delta_j = -1; delta_j <= 1; ++delta_j)
    {
      if (delta_i != 0 || delta_j != 0)
      {
        int ip = i + delta_i;
        int jp = j + delta_j;
        if (ip < (int)I && jp < (int)J && ip >= 0 && jp >= 0)
        {
          puintVec.push_back(std::make_pair((unsigned int)ip, (unsigned int)jp));
        }
      }
    }
  }
  // Return result
  return puintVec;
}

bool WordAlignmentMatrix::ijInNeighbourhood(unsigned int i, unsigned int j)
{
  if (i > 0)
    if (matrix[i - 1][j] != 0)
      return 1;
  if (j > 0)
    if (matrix[i][j - 1] != 0)
      return 1;
  if (i < I - 1)
    if (matrix[i + 1][j] != 0)
      return 1;
  if (j < J - 1)
    if (matrix[i][j + 1] != 0)
      return 1;

  return 0;
}

bool WordAlignmentMatrix::ijHasHorizNeighbours(unsigned int i, unsigned int j)
{
  if (j > 0)
    if (matrix[i][j - 1] != 0)
      return 1;
  if (j < J - 1)
    if (matrix[i][j + 1] != 0)
      return 1;

  return 0;
}

bool WordAlignmentMatrix::ijHasVertNeighbours(unsigned int i, unsigned int j)
{
  if (i > 0)
    if (matrix[i - 1][j] != 0)
      return 1;
  if (i < I - 1)
    if (matrix[i + 1][j] != 0)
      return 1;

  return 0;
}

bool WordAlignmentMatrix::jAligned(unsigned int j) const
{
  unsigned int i;

  for (i = 0; i < I; ++i)
    if (matrix[i][j] != 0)
      return 1;

  return 0;
}

bool WordAlignmentMatrix::iAligned(unsigned int i) const
{
  unsigned int j;

  for (j = 0; j < J; ++j)
    if (matrix[i][j] != 0)
      return 1;

  return 0;
}

void WordAlignmentMatrix::clear(void)
{
  unsigned int i;

  if (I > 0)
  {
    for (i = 0; i < I; ++i)
      free(matrix[i]);
    free(matrix);
  }
  I = 0;
  J = 0;
}

std::ostream& operator<<(std::ostream& outS, const WordAlignmentMatrix& waMatrix)
{
  unsigned int j;
  int i;

  for (i = (int)waMatrix.I - 1; i >= 0; --i)
  {
    for (j = 0; j < waMatrix.J; ++j)
      outS << (unsigned int)waMatrix.matrix[i][j] << " ";
    outS << std::endl;
  }
  return outS;
}

void WordAlignmentMatrix::print(FILE* f)
{
  unsigned int j;
  int i;

  for (i = (int)this->I - 1; i >= 0; --i)
  {
    for (j = 0; j < this->J; ++j)
      fprintf(f, "%d ", this->matrix[i][j]);
    fprintf(f, "\n");
  }
}

void WordAlignmentMatrix::wordAligAsVectors(std::vector<std::pair<unsigned int, unsigned int>>& sourceSegm,
                                            std::vector<unsigned int>& targetCuts)
{
  std::pair<unsigned int, unsigned int> prevIntPair, intPair;
  unsigned int i, j;

  targetCuts.clear();

  prevIntPair.first = 0;
  prevIntPair.second = 0;
  for (i = 0; i < I; ++i)
  {
    intPair.first = 0;
    intPair.second = 0;
    for (j = 0; j < J; ++j)
    {
      if (matrix[i][j] != 0 && intPair.first == 0)
        intPair.first = j + 1;
      if (matrix[i][j] == 0 && intPair.first != 0 && intPair.second == 0)
        intPair.second = j;
    }
    if (intPair.second == 0)
      intPair.second = j;
    if (intPair != prevIntPair)
    {
      sourceSegm.push_back(intPair);
      if (i != 0)
        targetCuts.push_back(i);
      prevIntPair = intPair;
    }
  }
  targetCuts.push_back(i);
}

WordAlignmentMatrix::~WordAlignmentMatrix()
{
  clear();
}
